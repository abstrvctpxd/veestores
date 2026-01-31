#!/usr/bin/env bash
# Start script for frontend service — ensures correct PYTHONPATH
exec gunicorn frontend.run:app --bind 0.0.0.0:${PORT:-5000} --pythonpath .
