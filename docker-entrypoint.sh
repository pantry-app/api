#!/bin/sh

# https://stackoverflow.com/a/33993532
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
# echo "Starting server"
# uwsgi --http :8000 --module api.wsgi --static-map /static=/code/staticfiles
uwsgi /code/uswgi.ini