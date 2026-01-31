<!-- Quick Start Guide for VeeStores E-Commerce Platform -->

# VeeStores - Quick Reference Guide

## 🚀 Start the Application

### Terminal 1 - Backend Server
```bash
cd backend
pip install -r requirements.txt
python run.py
# Runs on http://localhost:5000
```

### Terminal 2 - Frontend Server
```bash
cd frontend
pip install -r requirements.txt
python run.py
# Runs on http://localhost:5001
```

## 📍 Access Points

| Component | URL | Purpose |
|-----------|-----|---------|
| Customer Store | http://localhost:5001 | Browse products, shopping |
| Admin Dashboard | http://localhost:5000/admin/ | Manage inventory & orders |
| API Health | http://localhost:5000/api/health | Check backend status |

## 📊 Admin Dashboard Features

### Dashboard
- View key metrics (Total Products, Categories, Orders, Revenue)
- See recent orders
- Real-time statistics

### Products Management
- View all products
- Create new products
- Edit existing products
- Delete products
- Manage stock levels
- Set product status (Active/Inactive)

### Categories Management
- Create product categories
- Edit categories
- Delete categories
- Card-based category view

### Orders Management
- View all orders
- Check order details with items
- Update order status
- Manage customer information
- Track shipping and delivery

## 🛍️ Customer Store Pages

### Home (`/`)
- Featured products showcase
- Key features highlight
- Newsletter subscription

### Products (`/products`)
- Browse all products
- Filter by price range
- Filter by category
- Filter by rating
- Sort by newest, price, popularity, rating
- Product grid display

### Cart (`/cart`)
- View items in cart
- Adjust quantities
- See order summary
- Proceed to checkout

### Other Pages
- `/product/<id>` - Individual product details
- `/checkout` - Checkout page
- `/about` - About VeeStores
- `/contact` - Contact form

## 🗄️ Database Models

### Product
```
- ID, Name, Description, Price, Quantity
- Category ID, Image URL, SKU
- Active Status, Created/Updated timestamps
```

### Category
```
- ID, Name, Description
- Created/Updated timestamps
```

### Order
```
- ID, Customer Name/Email/Phone
- Shipping Address, Total Amount
- Status (Pending/Processing/Shipped/Delivered/Cancelled)
- Created/Updated timestamps
```

### OrderItem
```
- ID, Order ID, Product ID
- Quantity, Unit Price
```

## 🎨 UI Features

### Design Elements
- **Navigation**: Sticky navbar with search
- **Sidebar**: Admin sidebar for easy navigation
- **Cards**: Product cards with hover effects
- **Badges**: Status indicators
- **Forms**: Clean form layouts
- **Tables**: Sortable data tables
- **Animations**: Smooth transitions

### Responsive Breakpoints
- Desktop: 1920px+
- Laptop: 1024px+
- Tablet: 768px+
- Mobile: 320px+

## 🔧 Customization

### Change Store Name
File: `frontend/app/templates/base.html`
```html
<span class="navbar-brand">YourStoreName</span>
```

### Change Colors
File: `frontend/app/templates/base.html` and `backend/app/templates/admin/base.html`
```css
--primary-color: #2c3e50;
--accent-color: #e74c3c;
--success-color: #27ae60;
```

### Add New Product Category
Via Admin UI: Go to Categories → Add Category
Or via API:
```bash
curl -X POST http://localhost:5000/api/categories \
  -H "Content-Type: application/json" \
  -d '{"name":"Category Name","description":"Description"}'
```

### Add New Product
Via Admin UI: Go to Products → Add New Product
Or via API:
```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name":"Product Name",
    "price":99.99,
    "category_id":1,
    "sku":"PROD-001",
    "quantity":10,
    "description":"Description"
  }'
```

## 📁 Important Files

### Backend
- `backend/config.py` - Configuration (Database, Secret Key)
- `backend/app/models/` - Database models
- `backend/app/routes/admin_routes.py` - Admin panel routes
- `backend/app/routes/api_routes.py` - API endpoints
- `backend/app/templates/admin/` - Admin HTML templates

### Frontend
- `frontend/app/routes/store_routes.py` - Store page routes
- `frontend/app/templates/` - Customer-facing HTML
- `frontend/app/templates/base.html` - Base layout with navbar/footer

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Check if port 5000 is in use
lsof -i :5000
# Kill process if needed
kill -9 <PID>
```

### Database Issues
```bash
# Delete and recreate database
rm backend/ecommerce.db
python backend/run.py  # Creates new database
```

### Frontend Can't Connect to Backend
1. Ensure backend is running on port 5000
2. Check `BACKEND_URL` in `frontend/app/routes/store_routes.py`
3. Verify firewall allows localhost communication

### CORS Issues
If frontend can't reach backend API, check backend for CORS setup

## 🚀 Deployment Preparation

Before deploying to production:

1. **Security**
   - [ ] Change SECRET_KEY in config.py
   - [ ] Use PostgreSQL instead of SQLite
   - [ ] Add CSRF protection
   - [ ] Implement rate limiting

2. **Authentication**
   - [ ] Add user login/register
   - [ ] Implement session management
   - [ ] Add admin authentication

3. **Performance**
   - [ ] Enable caching (Redis)
   - [ ] Optimize images
   - [ ] Add database indexes
   - [ ] Implement CDN for static files

4. **Monitoring**
   - [ ] Add logging
   - [ ] Set up error tracking
   - [ ] Add performance monitoring
   - [ ] Implement backup strategy

## 📞 Support

For detailed information:
- Check `README.md` in root directory
- Check `backend/README.md` for backend details
- Check `frontend/README.md` for frontend details
- Review inline code comments

---

**Built with Flask and Bootstrap 5**
