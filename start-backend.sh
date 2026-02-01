#!/usr/bin/env bash
# Start script for backend service — ensures correct PYTHONPATH
exec gunicorn backend.run:app --bind 0.0.0.0:${PORT:-5000} --pythonpath .
