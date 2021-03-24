import os

from django.core.management import CommandError

os.system("python manage.py makemigrations "
          "&& python manage.py migrate")

DJANGO_SUPERUSER_USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME')
DJANGO_SUPERUSER_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')

if DJANGO_SUPERUSER_USERNAME:
    try:
        os.system(f"python manage.py createsuperuser \
            --noinput \
            --username {DJANGO_SUPERUSER_USERNAME} \
            --email {DJANGO_SUPERUSER_EMAIL}")

    except CommandError:
        print("The superuser was not created")

os.system("python manage.py runserver 0.0.0.0:8000")
