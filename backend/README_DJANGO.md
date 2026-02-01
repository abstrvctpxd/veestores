This folder now contains a minimal Django scaffold for the veestores backend.

Usage:

Install dependencies (from repo root):

    pip install -r backend/requirements.txt

Run locally:

    cd backend
    python manage.py migrate
    python manage.py runserver

Production start (Render): uses `gunicorn veestores_django.wsgi:application`.
