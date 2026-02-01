#!/usr/bin/env bash
# Start Django app: change into backend and run gunicorn
cd "$(dirname "$0")"
exec gunicorn veestores_django.wsgi:application --bind 0.0.0.0:${PORT:-5000} --pythonpath .
