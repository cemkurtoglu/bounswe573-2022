#!/bin/bash

# Collect static files
# echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate user_profile_page_settings --noinput || exit 1

# Start server
echo "Starting server"
gunicorn coLearning_website.wsgi:application --bind 0.0.0.0:8000