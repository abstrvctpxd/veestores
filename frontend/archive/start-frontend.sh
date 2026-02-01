#!/usr/bin/env bash
# Frontend start script: change into frontend directory then run gunicorn
cd "$(dirname "$0")"
exec gunicorn run:app --bind 0.0.0.0:${PORT:-5000} --pythonpath .
