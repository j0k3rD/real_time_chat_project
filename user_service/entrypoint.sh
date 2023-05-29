#!/bin/bash

# Create superuser
# python3 manage.py makemigrations
# python3 manage.py migrate
# export DJANGO_SUPERUSER_USERNAME=XXXXXX
# export DJANGO_SUPERUSER_PASSWORD=XXXXXX
# python3 manage.py createsuperuser --noinput

# Run server
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:9000