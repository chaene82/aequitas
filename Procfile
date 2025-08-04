web: gunicorn --pythonpath app app.wsgi:application --bind 0.0.0.0:$PORT
release: python app/manage.py migrate