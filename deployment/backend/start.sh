#!/bin/bash

# Run migrations, collect static files and start server
if [ "$APP_ENV" != "prod" ]; then
    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
    python manage.py runserver "$APP_HOST":"$APP_PORT"
else
    python manage.py makemigrations --noinput
    python manage.py migrate --noinput
fi
