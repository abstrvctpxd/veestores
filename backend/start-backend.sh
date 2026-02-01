#!/usr/bin/env bash
# Backend start script inside backend/ directory
exec gunicorn backend.run:app --bind 0.0.0.0:${PORT:-5000} --pythonpath ..
