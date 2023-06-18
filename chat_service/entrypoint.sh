#!/bin/bash

# Create superuser
# python3 manage.py migrate
# export DJANGO_SUPERUSER_USERNAME=XXXXXX
# export DJANGO_SUPERUSER_PASSWORD=XXXXXX
# export DJANGO_SUPERUSER_EMAIL=XXXXXX@XXXXXX.com
# python3 manage.py createsuperuser --noinput

# Run server
#python3 manage.py makemigrations (NO ACTIVAR A NO SER QUE SE HAYAN HECHO CAMBIOS EN LOS MODELOS)
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:7000