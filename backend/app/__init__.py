from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name='development'):
    """Create and configure Flask app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.routes import admin_routes, api_routes
    app.register_blueprint(admin_routes.bp)
    app.register_blueprint(api_routes.bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
