#!/bin/bash

pip-sync requirements.txt
python manage.py migrate

# uwsgi --ini /app/docker/service/uwsgi_dev.ini


python manage.py runserver 0.0.0.0:3000
