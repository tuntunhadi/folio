#!/bin/bash
# ─────────────────────────────────────────────────
#  WikiKu — Setup Script
# ─────────────────────────────────────────────────

echo ""
echo "  📚 WikiKu Setup"
echo "─────────────────────────────────────────────"

# 1. Create virtual environment
echo "▶ Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
echo "▶ Installing dependencies..."
pip install -r requirements.txt --quiet

# 3. Run migrations
echo "▶ Running database migrations..."
python manage.py migrate

# 4. Create superuser
echo ""
echo "─────────────────────────────────────────────"
echo "  Create your Admin account"
echo "─────────────────────────────────────────────"
python manage.py createsuperuser

echo ""
echo "─────────────────────────────────────────────"
echo "  ✅ Setup complete!"
echo ""
echo "  Run the server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "  Then open: http://127.0.0.1:8000"
echo "─────────────────────────────────────────────"
echo ""
