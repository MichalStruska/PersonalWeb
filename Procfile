web: python manage.py runserver 0.0.0.0:5000
release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn website.wsgi
