#!/bin/bash
PORT=${PORT:-8000}

if [ "$RUN_MIGRATIONS" = "1" ]; then
    echo "Running migrations..."
    python manage.py migrate --noinput
    python manage.py loaddata dump.json
fi

echo "Starting Gunicorn..."
gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
