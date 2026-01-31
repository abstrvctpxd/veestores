# 🚀 VeeStores - Getting Started Checklist

## Pre-Flight Check

- [ ] Python 3.8+ installed
- [ ] pip installed
- [ ] Git installed (already in repo)
- [ ] 2 terminal windows available
- [ ] Ports 5000 and 5001 are free

---

## Initial Setup (First Time Only)

### Step 1: Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```
**Expected:** No errors, all packages installed

### Step 2: Install Frontend Dependencies
```bash
cd ../frontend
pip install -r requirements.txt
```
**Expected:** No errors, all packages installed

---

## Start the Application

### Terminal 1: Start Backend
```bash
cd backend
python run.py
```
**Expected Output:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Terminal 2: Start Frontend
```bash
cd frontend
python run.py
```
**Expected Output:**
```
 * Running on http://127.0.0.1:5001
 * Debug mode: on
```

---

## Access the Application

Once both servers are running:

### 🛍️ Customer Store
```
URL: http://localhost:5001
- Browse this in your browser
- See the home page with featured products
- Test navigation
```

### 📊 Admin Dashboard
```
URL: http://localhost:5000/admin/
- Access the admin dashboard
- See the dashboard with statistics
- Add some test data
```

### 🔌 API Health Check
```
URL: http://localhost:5000/api/health
- Check backend API status
- Should return: {"status": "healthy"}
```

---

## Quick Test Workflow

### 1. Create a Category
Go to: http://localhost:5000/admin/categories
- Click "Add Category"
- Enter: Name = "Electronics", Description = "Electronic devices"
- Click "Create Category"
- ✓ Category created!

### 2. Create a Product
Go to: http://localhost:5000/admin/products
- Click "Add New Product"
- Fill in details:
  - Name: "Laptop Pro"
  - Price: 999.99
  - Category: Electronics
  - SKU: LAPTOP-001
  - Quantity: 10
- Click "Create Product"
- ✓ Product created!

### 3. View in Customer Store
Go to: http://localhost:5001/products
- Should see your product listed
- Filter and sort options work
- ✓ Products showing!

### 4. Add to Cart
- Click "Add to Cart"
- Cart badge updates
- Go to /cart
- ✓ Cart working!

---

## Verification Checklist

After starting both servers, verify:

- [ ] Backend running on port 5000
- [ ] Frontend running on port 5001
- [ ] No error messages in either terminal
- [ ] Can access http://localhost:5001
- [ ] Can access http://localhost:5000/admin/
- [ ] Admin dashboard shows statistics
- [ ] Database file created (backend/ecommerce.db)
- [ ] Can create products in admin
- [ ] Products appear in customer store
- [ ] Navigation works
- [ ] Footer displays correctly
- [ ] Responsive design works (try resizing browser)

---

## Common Issues & Solutions

### Issue: Port 5000 or 5001 already in use

**Solution 1:** Kill existing process
```bash
# Find process using port 5000
lsof -i :5000

# Kill it (if needed)
kill -9 <PID>
```

**Solution 2:** Use different ports
Edit `run.py` files and change:
```python
# Change from:
app.run(debug=True, port=5000)

# To:
app.run(debug=True, port=5002)
```

### Issue: `ModuleNotFoundError` when running

**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Database errors

**Solution:** Recreate database
```bash
cd backend
rm ecommerce.db
python run.py  # Creates new database
```

### Issue: Can't connect frontend to backend

**Solution:** 
1. Verify backend is running on port 5000
2. Check `BACKEND_URL` in `frontend/app/routes/store_routes.py`
3. Current value should be: `http://localhost:5000/api`

### Issue: Static files not loading (CSS looks broken)

**Solution:** Restart Flask servers
- Ctrl+C in both terminals
- Re-run `python run.py` in each

---

## File Structure Overview

```
veestores/
├── backend/                    # Backend API & Admin
│   ├── app/
│   │   ├── models/            # Database models
│   │   ├── routes/            # Routes
│   │   └── templates/         # Admin templates
│   ├── config.py
│   ├── run.py                 ← Start here
│   └── ecommerce.db           # Created automatically
│
├── frontend/                   # Customer store
│   ├── app/
│   │   ├── routes/
│   │   ├── templates/
│   │   └── static/
│   └── run.py                 ← Start here
│
├── README.md                  # Main docs
├── QUICK_START.md            # Quick reference
├── BUILD_SUMMARY.md          # Build details
├── ARCHITECTURE.md           # System architecture
└── GETTING_STARTED.md        # This file
```

---

## Next Steps After Verification

### Immediate (Today)
1. ✓ Backend and frontend running
2. ✓ Admin dashboard accessible
3. ✓ Create test data (categories, products)
4. ✓ Verify customer store works

### Short Term (This Week)
1. Customize colors and branding
2. Add more products
3. Test checkout flow
4. Create test orders
5. Review admin dashboard features

### Medium Term (Next Week)
1. Add user authentication
2. Integrate payment processing
3. Set up email notifications
4. Create additional admin reports
5. Optimize performance

### Long Term (Next Month+)
1. Deploy to production
2. Add more features
3. Implement analytics
4. Scale infrastructure
5. Regular maintenance

---

## Documentation Reference

| Document | Purpose |
|----------|---------|
| README.md | Complete project documentation |
| QUICK_START.md | Quick reference and commands |
| BUILD_SUMMARY.md | Detailed feature overview |
| ARCHITECTURE.md | System design and flow |
| GETTING_STARTED.md | This file - setup instructions |
| backend/README.md | Backend-specific docs |
| frontend/README.md | Frontend-specific docs |

---

## Key URLs for Quick Access

```
Customer Store:      http://localhost:5001
Admin Dashboard:     http://localhost:5000/admin/
API Health:          http://localhost:5000/api/health
```

---

## Keyboard Shortcuts for Development

### Restart Servers
```
Ctrl+C in terminal to stop
python run.py to start
```

### View Logs
- Keep both terminals visible
- Errors appear in real-time
- Useful for debugging

### Database Changes
- Changes appear immediately
- No restart needed for data changes
- Restart only if models change

---

## Performance Tips

### During Development
1. Keep both servers running
2. Reload browser after making changes
3. Use browser developer tools (F12)
4. Check terminal for error messages

### Browser Testing
1. Test in Chrome (primary)
2. Test in Firefox (compatibility)
3. Test mobile view (F12 → Toggle device)
4. Clear cache if changes don't appear

---

## Security Reminder

This is a development setup. Before going to production:

1. [ ] Change SECRET_KEY in backend/config.py
2. [ ] Use PostgreSQL instead of SQLite
3. [ ] Add authentication for admin access
4. [ ] Enable HTTPS/SSL
5. [ ] Add input validation
6. [ ] Implement CSRF protection
7. [ ] Set up logging and monitoring
8. [ ] Regular database backups

---

## Quick Commands Reference

```bash
# Start backend
cd backend && python run.py

# Start frontend
cd frontend && python run.py

# Install dependencies
pip install -r requirements.txt

# Reset database (backend)
rm backend/ecommerce.db

# Check if port is in use
lsof -i :5000  # or :5001

# Kill process on port
kill -9 <PID>
```

---

## Support & Help

### If Something Breaks
1. Check the error message in terminal
2. Review the issue in the troubleshooting section
3. Check relevant README.md file
4. Try restarting both servers
5. Check if database needs to be recreated

### Check These Files
- [BUILD_SUMMARY.md](BUILD_SUMMARY.md) - Complete feature list
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design
- [backend/README.md](backend/README.md) - Backend docs
- [frontend/README.md](frontend/README.md) - Frontend docs

---

## Success Criteria ✅

You'll know everything is working when:

1. ✅ Both servers start without errors
2. ✅ Can navigate to http://localhost:5001
3. ✅ Can access http://localhost:5000/admin/
4. ✅ Can see admin dashboard with stats
5. ✅ Can add categories and products
6. ✅ Products appear in customer store
7. ✅ Cart functionality works
8. ✅ Navigation is responsive
9. ✅ No console errors in browser
10. ✅ Database file exists (ecommerce.db)

---

## Ready to Start?

```bash
# Terminal 1 - Backend
cd backend
python run.py

# Terminal 2 - Frontend (in new terminal)
cd frontend
python run.py

# Then open browser
# http://localhost:5001
```

**🎉 You're all set! Start building your e-commerce store!**

---

**Questions? Check the README.md or ARCHITECTURE.md files for more detailed information.**

**Happy Coding! 🚀**
