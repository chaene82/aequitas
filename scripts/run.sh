#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

# Use gunicorn if GUNICORN env var is set, otherwise use uwsgi
if [ "$USE_GUNICORN" = "1" ]; then
    gunicorn --bind 0.0.0.0:9000 --workers 4 app.wsgi:application
else
    uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
fi