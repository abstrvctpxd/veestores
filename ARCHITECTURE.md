# VeeStores Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    VeeStores E-Commerce                     │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
         ┌──────▼──────┐            ┌──────▼──────┐
         │  Frontend   │            │  Backend    │
         │  (Port 5001)│            │ (Port 5000) │
         └──────┬──────┘            └──────┬──────┘
                │                          │
         ┌──────▼──────┐            ┌──────▼──────┐
         │  Customer   │            │    Admin    │
         │    Store    │            │  Dashboard  │
         └─────────────┘            └──────┬──────┘
                │                          │
                │                    ┌─────▼─────┐
                │                    │  REST API  │
                │                    └─────┬─────┘
                │                          │
                └──────────┬───────────────┘
                           │
                      ┌────▼─────┐
                      │ SQLite DB │
                      │(ecommerce │
                      │   .db)    │
                      └───────────┘
```

## Data Flow

### Product Management Flow
```
Admin User
    │
    ▼
Admin Dashboard (http://localhost:5000/admin/products)
    │
    ├─► View Products ─────────► List from DB
    ├─► Add Product ────────────► Insert to DB
    ├─► Edit Product ───────────► Update DB
    └─► Delete Product ─────────► Delete from DB
```

### Customer Shopping Flow
```
Customer
    │
    ▼
Frontend Store (http://localhost:5001)
    │
    ├─► Browse Products ────────► Fetch from API ──► DB
    ├─► View Product Details ──► Fetch from API ──► DB
    ├─► Add to Cart ───────────► Local Storage
    └─► Checkout ──────────────► Create Order ────► DB
```

### API Integration
```
Frontend Store Request
    │
    ▼
Flask Backend (http://localhost:5000/api)
    │
    ├─► GET /api/products ──────────► Query Products Table
    ├─► GET /api/categories ────────► Query Categories Table
    ├─► POST /api/orders ───────────► Insert Order + Items
    └─► GET /api/orders ───────────► Query Orders Table
    │
    ▼
SQLAlchemy ORM
    │
    ▼
SQLite Database
```

## Database Schema

```
┌─────────────────────────────────────────────────────────────┐
│                      CATEGORIES                             │
├────────────────────────────────────────────────────────────┤
│ id (PK)  │ name │ description │ created_at │ updated_at  │
└─────────────────────────────────────────────────────────────┘
                        │
                        │ (1:Many)
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      PRODUCTS                               │
├────────────────────────────────────────────────────────────┤
│ id (PK) │ name │ price │ quantity │ category_id (FK)    │
│ description │ image_url │ sku │ is_active │ timestamps  │
└─────────────────────────────────────────────────────────────┘
                        │
                        │ (1:Many)
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    ORDER_ITEMS                              │
├────────────────────────────────────────────────────────────┤
│ id (PK) │ order_id (FK) │ product_id (FK)                 │
│ quantity │ unit_price                                      │
└─────────────────────────────────────────────────────────────┘
        ▲
        │ (1:Many)
        │
┌─────────────────────────────────────────────────────────────┐
│                      ORDERS                                 │
├────────────────────────────────────────────────────────────┤
│ id (PK) │ customer_name │ customer_email │ customer_phone │
│ shipping_address │ total_amount │ status │ timestamps    │
└─────────────────────────────────────────────────────────────┘
```

## Frontend Components

```
┌─────────────────────────────────────────────┐
│              BASE LAYOUT                    │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │     Navigation Bar (Sticky)          │  │
│  │  [Logo] [Search] [Links] [Cart]      │  │
│  └──────────────────────────────────────┘  │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │         Main Content Area            │  │
│  │    (Page-specific content here)      │  │
│  └──────────────────────────────────────┘  │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │     Footer (Links, Social Media)     │  │
│  └──────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

## Admin Components

```
┌─────────────────────────────────────────────────────┐
│              ADMIN LAYOUT                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────┐ ┌────────────────────────────────┐  │
│  │  SIDEBAR │ │        MAIN CONTENT            │  │
│  ├──────────┤ ├────────────────────────────────┤  │
│  │          │ │  Dashboard / Products /        │  │
│  │ Dashboard│ │  Categories / Orders           │  │
│  │          │ │                                │  │
│  │ Products │ │  ┌──────────────────────────┐ │  │
│  │          │ │  │  Statistics Cards        │ │  │
│  │Categories│ │  ├──────────────────────────┤ │  │
│  │          │ │  │  Data Tables             │ │  │
│  │ Orders   │ │  │  Forms                   │ │  │
│  │          │ │  │  Management Tools        │ │  │
│  │ ...      │ │  └──────────────────────────┘ │  │
│  │          │ │                                │  │
│  │ Logout   │ │                                │  │
│  │          │ │                                │  │
│  └──────────┘ └────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Request/Response Flow

### GET Product Request
```
┌─────────────────────────────────────────────────────────────┐
│ Frontend: GET /products                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Backend: @app.route('/api/products')                        │
│ - Query all products from database                          │
│ - Convert to JSON format                                    │
│ - Return response                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ JSON Response:                                              │
│ [                                                           │
│   {                                                         │
│     "id": 1,                                               │
│     "name": "Laptop Pro",                                   │
│     "price": 999.99,                                        │
│     "quantity": 10,                                         │
│     "category_name": "Electronics"                          │
│   },                                                        │
│   ...                                                       │
│ ]                                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Frontend: Render products on page                           │
│ - Create product cards                                      │
│ - Display with images and prices                           │
│ - Add to cart buttons                                       │
└─────────────────────────────────────────────────────────────┘
```

## File Organization

### Backend Structure
```
backend/
├── config.py          ← Configuration (database, env settings)
├── run.py             ← Entry point (python run.py)
├── requirements.txt   ← Python dependencies
├── app/
│   ├── __init__.py    ← Flask app factory
│   ├── models/        ← Database models
│   │   ├── product.py
│   │   ├── category.py
│   │   ├── order.py
│   │   └── order_item.py
│   ├── routes/        ← Route handlers
│   │   ├── admin_routes.py    (Dashboard routes)
│   │   └── api_routes.py       (API endpoints)
│   └── templates/     ← HTML templates (Jinja2)
│       └── admin/
│           ├── base.html
│           ├── dashboard.html
│           ├── products.html
│           └── ...
└── ecommerce.db       ← SQLite database (auto-created)
```

### Frontend Structure
```
frontend/
├── run.py             ← Entry point (python run.py)
├── requirements.txt   ← Python dependencies
├── app/
│   ├── __init__.py    ← Flask app factory
│   ├── routes/        ← Route handlers
│   │   └── store_routes.py     (Page routes)
│   ├── templates/     ← HTML templates (Jinja2)
│   │   ├── base.html           (Base layout)
│   │   ├── index.html          (Home page)
│   │   ├── products.html       (Products page)
│   │   ├── cart.html           (Shopping cart)
│   │   └── ...
│   └── static/        ← Static files (CSS, JS, images)
│       ├── css/
│       ├── js/
│       └── images/
└── .env               ← Environment variables (optional)
```

## Key Technologies & Versions

```
Backend:
├── Flask 2.3.3 ..................... Web framework
├── SQLAlchemy 2.0.21 ............... ORM
├── Flask-SQLAlchemy 3.0.5 .......... Flask integration
├── Werkzeug 2.3.7 .................. WSGI utilities
└── click 8.1.7 ..................... CLI utilities

Frontend:
├── Flask 2.3.3 ..................... Web framework
├── requests 2.31.0 ................. HTTP library
├── Bootstrap 5 (CDN) ............... CSS framework
├── Bootstrap Icons (CDN) ........... Icon library
└── Jinja2 (built-in) ............... Template engine

Database:
└── SQLite .......................... File-based database
```

## Environment Setup

```
Step 1: Install Python 3.8+
         │
         ▼
Step 2: Navigate to backend
         │
         ▼
Step 3: pip install -r requirements.txt
         │
         ▼
Step 4: python run.py
         │
         ▼
Backend Running on http://localhost:5000
         │
         ▼
Step 5: In new terminal, navigate to frontend
         │
         ▼
Step 6: pip install -r requirements.txt
         │
         ▼
Step 7: python run.py
         │
         ▼
Frontend Running on http://localhost:5001
         │
         ▼
✓ System Ready!
```

## Access Points

```
Customer Store      ──────► http://localhost:5001
    ├─ Home
    ├─ Products
    ├─ Product Details
    ├─ Cart
    ├─ Checkout
    ├─ About
    └─ Contact

Admin Dashboard     ──────► http://localhost:5000/admin/
    ├─ Dashboard (Stats)
    ├─ Products Management
    ├─ Categories Management
    ├─ Orders Management
    └─ Order Details

API Endpoints       ──────► http://localhost:5000/api/
    ├─ /products
    ├─ /categories
    ├─ /orders
    └─ /health
```

---

**This architecture provides a scalable, maintainable e-commerce platform ready for development and deployment.**
