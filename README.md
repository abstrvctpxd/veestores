# VeeStores - E-Commerce Platform

A modern, full-stack e-commerce platform built with Flask, featuring a sleek user interface and a powerful admin dashboard for CRUD operations.

## 📁 Project Structure

```
veestores/
├── backend/              # Flask backend API & admin panel
│   ├── app/
│   │   ├── models/      # Database models (Product, Category, Order, OrderItem)
│   │   ├── routes/      # API routes and admin routes
│   │   ├── templates/   # Admin Jinja2 templates
│   │   └── __init__.py  # Flask app factory
│   ├── config.py        # Configuration settings
│   ├── run.py           # Entry point
│   └── requirements.txt # Backend dependencies
│
└── frontend/            # Flask frontend customer store
    ├── app/
    │   ├── routes/      # Store routes
    │   ├── templates/   # Customer-facing Jinja2 templates
    │   ├── static/      # CSS & assets
    │   └── __init__.py  # Flask app factory
    ├── run.py           # Entry point
    └── requirements.txt # Frontend dependencies
```

## ✨ Features

### Backend
- **RESTful API**: Full CRUD endpoints for products, categories, and orders
- **Database Models**: SQLAlchemy ORM with Product, Category, Order, and OrderItem models
- **Admin Dashboard**: Beautiful admin interface for managing inventory and orders
- **Status Tracking**: Order status management (Pending, Processing, Shipped, Delivered, Cancelled)

### Frontend
- **Product Browsing**: Browse products with categories and filtering
- **Shopping Cart**: Add to cart functionality
- **Responsive Design**: Mobile-friendly Bootstrap 5 interface
# VeeStores

Lightweight Flask e-commerce (frontend + backend). Designed for quick deployment and easy customization.

Quick start (development):

1) Install deps:
```
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

2) Start backend (defaults to SQLite). Set admin and DB as env vars if needed:
```
cd backend
set ADMIN_EMAIL=admin@veestores.com
set ADMIN_PASSWORD=admin1234
python run.py
```

3) Start frontend:
```
cd frontend
python run.py
```

Notes:
- Admin seeded by default: admin@veestores.com / admin1234 (change via `ADMIN_EMAIL`/`ADMIN_PASSWORD`).
- Use `DATABASE_URL` to connect to PostgreSQL in production.
- `BACKEND_API` env var lets the frontend point to a remote backend.
- Checkout supports a 50% deposit option (pay now, rest on delivery).

If you'd like, I can: run a local smoke test, wire a payment gateway stub, or prepare Render deployment steps.

