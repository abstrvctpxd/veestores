# Backend Configuration

## Running the Backend

```bash
cd backend
pip install -r requirements.txt
python run.py
```

Server runs on: `http://localhost:5000`

## Admin Dashboard

Access at: `http://localhost:5000/admin/`

### Features
- Dashboard with key metrics
- Product management (Create, Read, Update, Delete)
- Category management
- Order management and tracking

## API Endpoints

### Health Check
- `GET /api/health` - Check if API is running

### Products
- `GET /api/products` - Get all products
- `GET /api/products/<id>` - Get product by ID
- `POST /api/products` - Create product
- `PUT /api/products/<id>` - Update product
- `DELETE /api/products/<id>` - Delete product

### Categories
- `GET /api/categories` - Get all categories
- `GET /api/categories/<id>` - Get category by ID
- `POST /api/categories` - Create category
- `PUT /api/categories/<id>` - Update category
- `DELETE /api/categories/<id>` - Delete category

### Orders
- `GET /api/orders` - Get all orders
- `GET /api/orders/<id>` - Get order by ID
- `POST /api/orders` - Create order
- `PUT /api/orders/<id>` - Update order
- `DELETE /api/orders/<id>` - Delete order

## Database

Default: SQLite (`ecommerce.db`)

To use PostgreSQL, update `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/ecommerce'
```

## Environment Variables

Create a `.env` file:
```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///ecommerce.db
```

## Troubleshooting

**Port already in use:**
```bash
python run.py --port 5002
```

**Database errors:**
```bash
rm ecommerce.db  # Delete old database
python run.py     # Will create new one
```
