from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, flash
from app import db
from app.models import Category, Product, Order, User
from functools import wraps

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.before_request
def require_admin_login():
    # Allow access to the admin login page
    if request.endpoint and request.endpoint.startswith('admin.login'):
        return
    # For other admin routes, require admin session
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login form"""
    if request.method == 'POST':
        email = request.form.get('email', '').lower().strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(email=email, is_admin=True).first()
        if user and user.check_password(password):
            session['admin_logged_in'] = True
            session['admin_id'] = user.id
            session['admin_email'] = user.email
            flash('Logged in as admin', 'success')
            return redirect(url_for('admin.dashboard'))

        flash('Invalid admin credentials', 'danger')

    return render_template('admin/login.html')


@bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_id', None)
    session.pop('admin_email', None)
    flash('Logged out', 'info')
    return redirect(url_for('admin.login'))

# ==================== DASHBOARD ====================
@bp.route('/', methods=['GET'])
def dashboard():
    """Admin dashboard"""
    total_products = Product.query.count()
    total_categories = Category.query.count()
    total_orders = Order.query.count()
    total_revenue = db.session.query(db.func.sum(Order.total_amount)).scalar() or 0
    
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_products=total_products,
                         total_categories=total_categories,
                         total_orders=total_orders,
                         total_revenue=total_revenue,
                         recent_orders=recent_orders)

# ==================== CATEGORIES ====================
@bp.route('/categories', methods=['GET'])
def categories():
    """List all categories"""
    categories = Category.query.all()
    return render_template('admin/categories.html', categories=categories)

@bp.route('/categories/new', methods=['GET', 'POST'])
def create_category():
    """Create new category"""
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        
        return redirect(url_for('admin.categories'))
    
    return render_template('admin/category_form.html', category=None)

@bp.route('/categories/<int:id>/edit', methods=['GET', 'POST'])
def edit_category(id):
    """Edit a category"""
    category = Category.query.get_or_404(id)
    
    if request.method == 'POST':
        category.name = request.form.get('name')
        category.description = request.form.get('description')
        db.session.commit()
        
        return redirect(url_for('admin.categories'))
    
    return render_template('admin/category_form.html', category=category)

@bp.route('/categories/<int:id>/delete', methods=['POST'])
def delete_category(id):
    """Delete a category"""
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    
    return redirect(url_for('admin.categories'))

# ==================== PRODUCTS ====================
@bp.route('/products', methods=['GET'])
def products():
    """List all products"""
    products = Product.query.all()
    return render_template('admin/products.html', products=products)

@bp.route('/products/new', methods=['GET', 'POST'])
def create_product():
    """Create new product"""
    categories = Category.query.all()
    
    if request.method == 'POST':
        product = Product(
            name=request.form.get('name'),
            description=request.form.get('description'),
            price=float(request.form.get('price')),
            quantity=int(request.form.get('quantity', 0)),
            category_id=int(request.form.get('category_id')),
            image_url=request.form.get('image_url'),
            sku=request.form.get('sku'),
            is_active=request.form.get('is_active') == 'on'
        )
        db.session.add(product)
        db.session.commit()
        
        return redirect(url_for('admin.products'))
    
    return render_template('admin/product_form.html', product=None, categories=categories)

@bp.route('/products/<int:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    """Edit a product"""
    product = Product.query.get_or_404(id)
    categories = Category.query.all()
    
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.price = float(request.form.get('price'))
        product.quantity = int(request.form.get('quantity', 0))
        product.category_id = int(request.form.get('category_id'))
        product.image_url = request.form.get('image_url')
        product.sku = request.form.get('sku')
        product.is_active = request.form.get('is_active') == 'on'
        db.session.commit()
        
        return redirect(url_for('admin.products'))
    
    return render_template('admin/product_form.html', product=product, categories=categories)

@bp.route('/products/<int:id>/delete', methods=['POST'])
def delete_product(id):
    """Delete a product"""
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('admin.products'))

# ==================== ORDERS ====================
@bp.route('/orders', methods=['GET'])
def orders():
    """List all orders"""
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin/orders.html', orders=orders)

@bp.route('/orders/<int:id>', methods=['GET'])
def view_order(id):
    """View order details"""
    order = Order.query.get_or_404(id)
    return render_template('admin/order_detail.html', order=order)

@bp.route('/orders/<int:id>/edit', methods=['GET', 'POST'])
def edit_order(id):
    """Edit an order"""
    order = Order.query.get_or_404(id)
    
    if request.method == 'POST':
        order.customer_name = request.form.get('customer_name')
        order.customer_email = request.form.get('customer_email')
        order.customer_phone = request.form.get('customer_phone')
        order.shipping_address = request.form.get('shipping_address')
        order.status = request.form.get('status')
        db.session.commit()
        
        return redirect(url_for('admin.view_order', id=id))
    
    return render_template('admin/order_form.html', order=order)

@bp.route('/orders/<int:id>/delete', methods=['POST'])
def delete_order(id):
    """Delete an order"""
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    
    return redirect(url_for('admin.orders'))
