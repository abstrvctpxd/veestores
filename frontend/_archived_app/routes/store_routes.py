from flask import Blueprint, render_template, session, request, redirect, url_for, flash, jsonify
from _archived_app.routes.auth_routes import login_required
import requests, os

bp = Blueprint('store', __name__)

BACKEND_URL = os.environ.get('BACKEND_API', 'http://localhost:5000/api')

@bp.route('/', methods=['GET'])
def index():
    products = []
    try:
        resp = requests.get(f'{BACKEND_URL}/products', timeout=5)
        if resp.status_code == 200:
            products = resp.json()[:6]
    except Exception:
        products = []

    return render_template('index.html', products=products)

@bp.route('/products', methods=['GET'])
@login_required
def products():
    try:
        response = requests.get(f'{BACKEND_URL}/products')
        products = response.json() if response.status_code == 200 else []
    except:
        products = []
    
    return render_template('products.html', products=products)

@bp.route('/product/<int:id>', methods=['GET'])
@login_required
def product_detail(id):
    try:
        response = requests.get(f'{BACKEND_URL}/products/{id}')
        product = response.json() if response.status_code == 200 else None
    except:
        product = None
    
    return render_template('product_detail.html', product=product)

@bp.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json() or {}
    product_id = data.get('product_id')
    qty = int(data.get('quantity', 1))
    if not product_id:
        return jsonify({'error': 'product_id required'}), 400

    try:
        resp = requests.get(f'{BACKEND_URL}/products/{product_id}', timeout=5)
        if resp.status_code != 200:
            return jsonify({'error': 'Product not found'}), 404
        product = resp.json()
    except Exception:
        return jsonify({'error': 'Backend unreachable'}), 500

    cart = session.get('cart', [])
    for item in cart:
        if item['id'] == product['id']:
            item['quantity'] = item.get('quantity', 1) + qty
            break
    else:
        cart.append({
            'id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'quantity': qty
        })

    session['cart'] = cart
    return jsonify({'cart_count': sum(i.get('quantity',1) for i in cart)})

@bp.route('/cart', methods=['GET'])
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        pay_deposit = request.form.get('pay_deposit') == 'on'

        cart_items = session.get('cart', [])
        if not cart_items:
            flash('Your cart is empty', 'warning')
            return redirect(url_for('store.products'))

        items = []
        for it in cart_items:
            items.append({
                'product_id': it['id'],
                'quantity': it.get('quantity',1),
                'unit_price': it['price']
            })

        payload = {
            'customer_name': name,
            'customer_email': email,
            'customer_phone': phone,
            'shipping_address': address,
            'items': items,
            'pay_deposit': pay_deposit
        }

        try:
            resp = requests.post(f'{BACKEND_URL}/orders', json=payload, timeout=10)
            if resp.status_code in (200,201):
                session['cart'] = []
                order = resp.json()
                flash('Order placed successfully', 'success')
                return render_template('checkout_success.html', order=order)
            else:
                flash('Failed to place order: ' + resp.text, 'danger')
        except Exception:
            flash('Unable to contact backend to place order', 'danger')

    cart_items = session.get('cart', [])
    return render_template('checkout.html', cart_items=cart_items)

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        pass
    return render_template('contact.html')
