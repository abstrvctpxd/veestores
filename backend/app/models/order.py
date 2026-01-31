from app import db
from datetime import datetime
from enum import Enum

class OrderStatus(Enum):
    """Order status enumeration"""
    PENDING = 'pending'
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

class Order(db.Model):
    """Order model"""
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(200), nullable=False)
    customer_email = db.Column(db.String(200), nullable=False)
    customer_phone = db.Column(db.String(20))
    shipping_address = db.Column(db.Text, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    deposit_amount = db.Column(db.Float, default=0)
    deposit_paid = db.Column(db.Boolean, default=False)
    payment_status = db.Column(db.String(50), default=OrderStatus.PENDING.value)
    status = db.Column(db.String(50), default=OrderStatus.PENDING.value)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'customer_phone': self.customer_phone,
            'shipping_address': self.shipping_address,
            'total_amount': self.total_amount,
            'deposit_amount': self.deposit_amount,
            'deposit_paid': self.deposit_paid,
            'payment_status': self.payment_status,
            'status': self.status,
            'items': [item.to_dict() for item in self.items],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def __repr__(self):
        return f'<Order {self.id}>'
