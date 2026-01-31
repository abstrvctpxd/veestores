#!/usr/bin/env bash
# Frontend start script inside frontend/ directory
exec gunicorn frontend.run:app --bind 0.0.0.0:${PORT:-5000} --pythonpath ..
