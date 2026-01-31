from flask import Blueprint, jsonify, request
from app import db
from app.models import Category, Product, Order, OrderItem
from app.models import User
from werkzeug.security import generate_password_hash

bp = Blueprint('api', __name__, url_prefix='/api')

# ==================== CATEGORIES ====================
@bp.route('/categories', methods=['GET'])
def get_categories():
    """Get all categories"""
    categories = Category.query.all()
    return jsonify([cat.to_dict() for cat in categories])

@bp.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    """Get a specific category"""
    category = Category.query.get_or_404(id)
    return jsonify(category.to_dict())

@bp.route('/categories', methods=['POST'])
def create_category():
    """Create a new category"""
    data = request.get_json()
    
    if not data or not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400
    
    category = Category(
        name=data['name'],
        description=data.get('description', '')
    )
    
    db.session.add(category)
    db.session.commit()
    return jsonify(category.to_dict()), 201

@bp.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    """Update a category"""
    category = Category.query.get_or_404(id)
    data = request.get_json()
    
    if 'name' in data:
        category.name = data['name']
    if 'description' in data:
        category.description = data['description']
    
    db.session.commit()
    return jsonify(category.to_dict())

@bp.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    """Delete a category"""
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'}), 204

# ==================== PRODUCTS ====================
@bp.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = Product.query.all()
    return jsonify([prod.to_dict() for prod in products])

@bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """Get a specific product"""
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())

@bp.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.get_json()
    
    required_fields = ['name', 'price', 'category_id', 'sku']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), 400
    
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=float(data['price']),
        quantity=int(data.get('quantity', 0)),
        category_id=int(data['category_id']),
        image_url=data.get('image_url', ''),
        sku=data['sku'],
        is_active=data.get('is_active', True)
    )
    
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    """Update a product"""
    product = Product.query.get_or_404(id)
    data = request.get_json()
    
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = float(data['price'])
    if 'quantity' in data:
        product.quantity = int(data['quantity'])
    if 'category_id' in data:
        product.category_id = int(data['category_id'])
    if 'image_url' in data:
        product.image_url = data['image_url']
    if 'sku' in data:
        product.sku = data['sku']
    if 'is_active' in data:
        product.is_active = data['is_active']
    
    db.session.commit()
    return jsonify(product.to_dict())

@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    """Delete a product"""
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 204

# ==================== ORDERS ====================
@bp.route('/orders', methods=['GET'])
def get_orders():
    """Get all orders"""
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    """Get a specific order"""
    order = Order.query.get_or_404(id)
    return jsonify(order.to_dict())

@bp.route('/orders', methods=['POST'])
def create_order():
    """Create a new order"""
    data = request.get_json()
    
    required_fields = ['customer_name', 'customer_email', 'shipping_address']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), 400
    
    order = Order(
        customer_name=data['customer_name'],
        customer_email=data['customer_email'],
        customer_phone=data.get('customer_phone', ''),
        shipping_address=data['shipping_address'],
        total_amount=0,
        status=data.get('status', 'pending')
    )

    db.session.add(order)
    db.session.flush()

    # Add items if provided
    items = data.get('items', [])
    total = 0
    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=int(item['quantity']),
            unit_price=float(item['unit_price'])
        )
        total += order_item.quantity * order_item.unit_price
        db.session.add(order_item)

    order.total_amount = total

    # Handle deposit/payment option: pay_deposit True means customer pays 50% now
    pay_deposit = data.get('pay_deposit', False)
    if pay_deposit:
        order.deposit_amount = round(total / 2.0, 2)
        order.deposit_paid = True
        order.payment_status = 'deposit_paid'
    else:
        order.deposit_amount = 0
        order.deposit_paid = False
        order.payment_status = 'pending'

    db.session.commit()
    return jsonify(order.to_dict()), 201

@bp.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    """Update an order"""
    order = Order.query.get_or_404(id)
    data = request.get_json()
    
    if 'customer_name' in data:
        order.customer_name = data['customer_name']
    if 'customer_email' in data:
        order.customer_email = data['customer_email']
    if 'customer_phone' in data:
        order.customer_phone = data['customer_phone']
    if 'shipping_address' in data:
        order.shipping_address = data['shipping_address']
    if 'status' in data:
        order.status = data['status']
    
    db.session.commit()
    return jsonify(order.to_dict())

@bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    """Delete an order"""
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 204

# ==================== HEALTH CHECK ====================
@bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


# ==================== AUTH ====================
@bp.route('/auth/register', methods=['POST'])
def api_register():
    data = request.get_json() or {}
    username = data.get('username', '').strip()
    email = (data.get('email') or '').lower().strip()
    password = data.get('password', '')

    if not username or not email or not password:
        return jsonify({'error': 'username, email and password required'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    user = User(username=username, email=email, is_admin=False)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@bp.route('/auth/login', methods=['POST'])
def api_login():
    data = request.get_json() or {}
    email = (data.get('email') or '').lower().strip()
    password = data.get('password', '')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid credentials'}), 400

    return jsonify({'user': user.to_dict()}), 200
