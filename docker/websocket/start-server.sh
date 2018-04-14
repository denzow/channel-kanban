#!/bin/bash

pip-sync requirements.txt
python manage.py migrate

# uwsgi --ini /app/docker/service/uwsgi_dev.ini

/usr/local/bin/daphne --root-path /app -b 0.0.0.0 -p 3000 application.asgi:application
