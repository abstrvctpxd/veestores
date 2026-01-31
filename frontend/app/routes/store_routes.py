from flask import Blueprint, render_template, session, request
import requests

bp = Blueprint('store', __name__)

BACKEND_URL = 'http://localhost:5000/api'

# ==================== STORE PAGES ====================
@bp.route('/', methods=['GET'])
def index():
    """Home page"""
    return render_template('index.html')

@bp.route('/products', methods=['GET'])
def products():
    """Product listing page"""
    try:
        response = requests.get(f'{BACKEND_URL}/products')
        products = response.json() if response.status_code == 200 else []
    except:
        products = []
    
    return render_template('products.html', products=products)

@bp.route('/product/<int:id>', methods=['GET'])
def product_detail(id):
    """Product detail page"""
    try:
        response = requests.get(f'{BACKEND_URL}/products/{id}')
        product = response.json() if response.status_code == 200 else None
    except:
        product = None
    
    return render_template('product_detail.html', product=product)

@bp.route('/cart', methods=['GET'])
def cart():
    """Shopping cart page"""
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Checkout page"""
    if request.method == 'POST':
        # Handle checkout logic
        pass
    
    cart_items = session.get('cart', [])
    return render_template('checkout.html', cart_items=cart_items)

@bp.route('/about', methods=['GET'])
def about():
    """About page"""
    return render_template('about.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        # Handle contact form
        pass
    return render_template('contact.html')
