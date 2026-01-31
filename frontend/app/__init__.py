from flask import Flask

def create_app():
    """Create and configure Flask app for frontend"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-frontend-secret-key'
    
    # Register blueprints
    from app.routes import store_routes, auth_routes
    app.register_blueprint(store_routes.bp)
    app.register_blueprint(auth_routes.auth_bp)
    
    return app
