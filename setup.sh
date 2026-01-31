#!/bin/bash

# VeeStores Setup Script

echo "🛒 VeeStores - E-Commerce Platform Setup"
echo "========================================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Setup Backend
echo "📦 Setting up Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
echo "✅ Backend setup complete!"
echo ""

# Setup Frontend
echo "📦 Setting up Frontend..."
cd ../frontend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
echo "✅ Frontend setup complete!"
echo ""

echo "🎉 Setup Complete!"
echo ""
echo "To run the application:"
echo ""
echo "Backend:"
echo "  cd backend"
echo "  source venv/bin/activate  # or: venv\Scripts\activate on Windows"
echo "  python run.py"
echo ""
echo "Frontend (in another terminal):"
echo "  cd frontend"
echo "  source venv/bin/activate  # or: venv\Scripts\activate on Windows"
echo "  python run.py"
echo ""
echo "Then visit:"
echo "  Customer Store: http://localhost:5001"
echo "  Admin Dashboard: http://localhost:5000/admin/"
