from flask import Blueprint, render_template, request, redirect, url_for, session, flash, current_app
from functools import wraps
import requests
import os

auth_bp = Blueprint('auth', __name__)

BACKEND_API = os.environ.get('BACKEND_API', 'http://localhost:5000/api')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash('Please login first', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
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
    if request.method == 'POST':
        email = request.form.get('email', '').lower().strip()
        password = request.form.get('password', '')
        try:
            resp = requests.post(f'{BACKEND_API}/auth/login', json={'email': email, 'password': password}, timeout=5)
            data = resp.json()
        except Exception:
            flash('Unable to contact backend. Try again later.', 'danger')
            return render_template('login.html')

        if resp.status_code != 200:
            flash(data.get('error', 'Invalid email or password'), 'danger')
            return render_template('login.html')

        user = data.get('user')
        if user.get('is_admin'):
            flash('Admin users must login via the admin panel', 'warning')
            return redirect(f"/admin/login")

        session['user_email'] = user.get('email')
        session['username'] = user.get('username')
        session['is_admin'] = user.get('is_admin', False)
        flash(f"Welcome {user.get('username')}!", 'success')
        return redirect(url_for('store.index'))
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').lower().strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
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
        
        try:
            resp = requests.post(f'{BACKEND_API}/auth/register', json={
                'username': username,
                'email': email,
                'password': password
            }, timeout=5)
            data = resp.json()
        except Exception:
            flash('Unable to contact backend. Try again later.', 'danger')
            return redirect(url_for('auth.register'))

        if resp.status_code != 201:
            flash(data.get('error', 'Registration failed'), 'danger')
            return redirect(url_for('auth.register'))

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('store.index'))

@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', 
                         username=session.get('username'),
                         email=session.get('user_email'),
                         is_admin=session.get('is_admin', False))
