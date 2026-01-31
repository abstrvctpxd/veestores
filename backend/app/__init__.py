from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import os
from flask_wtf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_mail import Mail
import stripe

db = SQLAlchemy()
csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address)
mail = Mail()

def create_app(config_name='development'):
    """Create and configure Flask app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # ensure secret key exists
    app.secret_key = app.config.get('SECRET_KEY')

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)
    mail.init_app(app)

    # Configure Stripe if key provided
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY', '')

    # Create database tables and perform safe auto-migration BEFORE importing routes
    with app.app_context():
        db.create_all()

        # Ensure order table has new columns (best-effort auto-migration)
        try:
            from sqlalchemy import inspect, text
            inspector = inspect(db.engine)
            if 'orders' in inspector.get_table_names():
                cols = [c['name'] for c in inspector.get_columns('orders')]
                # Add missing columns using session execute and commit
                if 'deposit_amount' not in cols:
                    try:
                        db.session.execute(text('ALTER TABLE orders ADD COLUMN deposit_amount FLOAT DEFAULT 0'))
                        db.session.commit()
                    except Exception:
                        db.session.rollback()
                if 'deposit_paid' not in cols:
                    try:
                        db.session.execute(text("ALTER TABLE orders ADD COLUMN deposit_paid INTEGER DEFAULT 0"))
                        db.session.commit()
                    except Exception:
                        db.session.rollback()
                if 'payment_status' not in cols:
                    try:
                        db.session.execute(text("ALTER TABLE orders ADD COLUMN payment_status VARCHAR(50) DEFAULT 'pending'"))
                        db.session.commit()
                    except Exception:
                        db.session.rollback()
        except Exception:
            # If inspector isn't available or DB doesn't support, skip auto-migration
            pass

        # Lazy import to avoid circulars and seed admin user
        from app.models import User
        from werkzeug.security import generate_password_hash

        admin_email = os.environ.get('ADMIN_EMAIL', 'veestores@outlook.com')
        admin_password = os.environ.get('ADMIN_PASSWORD', 'admin1234')

        admin = User.query.filter_by(email=admin_email).first()
        if not admin:
            admin = User(username='Admin', email=admin_email, is_admin=True)
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()

    # Register blueprints after DB setup so routes import sees migrated schema
    from app.routes import admin_routes, api_routes
    app.register_blueprint(admin_routes.bp)
    app.register_blueprint(api_routes.bp)

    return app
