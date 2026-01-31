import os

class Config:
    """Base configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

class DevelopmentConfig(Config):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommerce.db'
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    _db_url = os.environ.get('DATABASE_URL', '')
    if _db_url and _db_url.startswith('postgres://'):
        _db_url = _db_url.replace('postgres://', 'postgresql+psycopg2://', 1)
    SQLALCHEMY_DATABASE_URI = _db_url or 'sqlite:///ecommerce.db'
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
