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
- **Navigation**: Easy-to-use navigation with search functionality
- **Pages**: Home, Products, About, Contact, Cart, Checkout

### UI/UX
- **Modern Design**: Gradient backgrounds and smooth animations
- **Bootstrap 5**: Professional, responsive layout
- **Color Scheme**: Professional blue (#2c3e50) and red (#e74c3c) theme
- **Smooth Animations**: Slide-in effects and hover animations

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
python run.py
```

The backend will start at `http://localhost:5000`

#### Admin Dashboard
- **URL**: `http://localhost:5000/admin/`
- **Features**: 
  - Dashboard with key metrics
  - Product management (Create, Read, Update, Delete)
  - Category management
  - Order management and tracking

#### API Endpoints
- `GET/POST /api/products` - Manage products
- `GET/POST /api/categories` - Manage categories
- `GET/POST /api/orders` - Manage orders
- `GET /api/health` - Health check

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the frontend server:
```bash
python run.py
```

The frontend will start at `http://localhost:5001`

#### Pages
- `/` - Home page with featured products
- `/products` - Product listing with filters
- `/product/<id>` - Product detail page
- `/cart` - Shopping cart
- `/checkout` - Checkout page
- `/about` - About page
- `/contact` - Contact page

## 🗄️ Database

The application uses SQLite by default. Database file: `ecommerce.db`

### Models

#### Product
- id, name, description, price, quantity, category_id, image_url, sku, is_active, created_at, updated_at

#### Category
- id, name, description, created_at, updated_at

#### Order
- id, customer_name, customer_email, customer_phone, shipping_address, total_amount, status, created_at, updated_at

#### OrderItem
- id, order_id, product_id, quantity, unit_price

## 🎨 Customization

### Colors
Edit CSS in templates:
```css
:root {
    --primary-color: #2c3e50;
    --accent-color: #e74c3c;
    --success-color: #27ae60;
}
```

## 📱 Responsive Design

Works on all devices: Desktop, Laptop, Tablet, Mobile

## 🔐 Security Notes

For production:
1. Change `SECRET_KEY` in config.py
2. Use PostgreSQL instead of SQLite
3. Implement proper user authentication
4. Add CSRF protection
5. Use HTTPS

## 🎯 Next Steps

1. Add user authentication (Login/Register)
2. Implement payment gateway integration
3. Add inventory notifications
4. Implement search functionality
5. Add product reviews and ratings
6. Add email notifications
7. Implement wishlist functionality

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

For issues or questions, please refer to the code comments or create an issue in the repository.

---

**Built with ❤️ using Flask and Bootstrap 5**
