python -m manage makemigrations
python -m manage migrate
gunicorn django_blog.wsgi:application --bind 0.0.0.0:8000