#!/bin/bash

# Create superuser
# python3 manage.py migrate
# export DJANGO_SUPERUSER_USERNAME=admin
# export DJANGO_SUPERUSER_PASSWORD=1234
# export DJANGO_SUPERUSER_EMAIL=admin@gmail.com
# python3 manage.py createsuperuser --noinput

# Run server
#python3 manage.py makemigrations (NO ACTIVAR A NO SER QUE SE HAYAN HECHO CAMBIOS EN LOS MODELOS)
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:9000