# Frontend Configuration

## Running the Frontend

```bash
cd frontend
pip install -r requirements.txt
python run.py
```

Server runs on: `http://localhost:5001`

## Pages

### Public Pages
- `/` - Home page
  - Featured products section
  - Key features highlight
  - Newsletter subscription
  
- `/products` - Product listing
  - Product filtering (price, category, rating)
  - Sorting options
  - Pagination
  
- `/product/<id>` - Product detail
  - Full product information
  - Add to cart button
  - Related products
  
- `/cart` - Shopping cart
  - View cart items
  - Adjust quantities
  - Order summary
  
- `/checkout` - Checkout page
  - Shipping information
  - Payment summary
  
- `/about` - About VeeStores
  - Company information
  - Key statistics
  
- `/contact` - Contact page
  - Contact form
  - Business information
  - Support options

## Features

- **Responsive Design**: Works on all devices
- **Bootstrap 5**: Professional styling
- **Bootstrap Icons**: Beautiful icon set
- **Smooth Animations**: CSS transitions and effects
- **Easy Navigation**: Clear menu structure

## Customization

### Change Store Name
Edit `app/templates/base.html`:
```html
<a class="navbar-brand" href="/">
    <i class="bi bi-shop"></i>YourStoreName
</a>
```

### Change Colors
Edit `app/templates/base.html` CSS variables:
```css
:root {
    --primary-color: #2c3e50;
    --accent-color: #e74c3c;
    --success-color: #27ae60;
}
```

### Add New Page
1. Create route in `app/routes/store_routes.py`
2. Create template in `app/templates/`
3. Add link to navigation in `app/templates/base.html`

## Backend Integration

The frontend connects to backend at: `http://localhost:5000/api`

Update in `app/routes/store_routes.py`:
```python
BACKEND_URL = 'http://localhost:5000/api'
```

## Static Files

CSS and JavaScript can be added to:
```
app/static/
├── css/
├── js/
└── images/
```

Reference in templates:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/custom.css') }}">
```

## Troubleshooting

**Can't connect to backend:**
1. Ensure backend is running on port 5000
2. Check `BACKEND_URL` in `store_routes.py`
3. Check firewall settings

**Static files not loading:**
- Flask cache issue - restart server
- Check file paths are correct

**Port in use:**
```bash
python run.py --port 5002
```
