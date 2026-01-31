from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

auth_bp = Blueprint('auth', __name__)

# Simple in-memory user storage for demo (replace with database in production)
USERS = {}

# Admin credentials (hardcoded for demo - in production use database)
ADMIN_USER = {
    'email': 'admin@veestores.com',
    'password_hash': generate_password_hash('admin123'),
    'username': 'Admin',
    'is_admin': True
}

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash('Please login first', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to require admin access"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash('Please login first', 'warning')
            return redirect(url_for('auth.login'))
        
        user_email = session.get('user_email')
        is_admin = session.get('is_admin', False)
        
        if not is_admin:
            flash('Admin access required', 'danger')
            return redirect(url_for('store.index'))
        
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login route"""
    if request.method == 'POST':
        email = request.form.get('email', '').lower().strip()
        password = request.form.get('password', '')
        
        # Check admin credentials
        if email == ADMIN_USER['email'] and check_password_hash(ADMIN_USER['password_hash'], password):
            session['user_email'] = email
            session['username'] = ADMIN_USER['username']
            session['is_admin'] = True
            flash('Welcome Admin! You are logged in.', 'success')
            return redirect(url_for('admin.dashboard'))
        
        # Check user credentials
        if email in USERS and check_password_hash(USERS[email]['password_hash'], password):
            session['user_email'] = email
            session['username'] = USERS[email]['username']
            session['is_admin'] = False
            flash(f'Welcome {USERS[email]["username"]}!', 'success')
            return redirect(url_for('store.index'))
        
        flash('Invalid email or password', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Register route"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').lower().strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validation
        if not username or len(username) < 3:
            flash('Username must be at least 3 characters', 'danger')
            return redirect(url_for('auth.register'))
        
        if not email or '@' not in email:
            flash('Please enter a valid email', 'danger')
            return redirect(url_for('auth.register'))
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.register'))
        
        if len(password) < 6:
            flash('Password must be at least 6 characters', 'danger')
            return redirect(url_for('auth.register'))
        
        # Check if email already exists
        if email in USERS or email == ADMIN_USER['email']:
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.register'))
        
        # Create user
        USERS[email] = {
            'username': username,
            'email': email,
            'password_hash': generate_password_hash(password),
            'is_admin': False
        }
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    """Logout route"""
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('store.index'))

@auth_bp.route('/profile')
@login_required
def profile():
    """User profile route"""
    return render_template('profile.html', 
                         username=session.get('username'),
                         email=session.get('user_email'),
                         is_admin=session.get('is_admin', False))
