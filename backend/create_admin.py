import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veestores_django.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

EMAIL = os.environ.get('ADMIN_EMAIL')
PASSWORD = os.environ.get('ADMIN_PASSWORD')

if not EMAIL or not PASSWORD:
    print('ADMIN_EMAIL or ADMIN_PASSWORD not set; skipping superuser creation')
else:
    if not User.objects.filter(email=EMAIL).exists():
        print(f'Creating admin user {EMAIL}')
        User.objects.create_superuser(username=EMAIL.split('@')[0], email=EMAIL, password=PASSWORD)
    else:
        print('Admin user already exists')
