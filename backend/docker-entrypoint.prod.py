import os
import multiprocessing

from django.core.management import CommandError

os.system("python manage.py makemigrations "
          "&& python manage.py migrate")
os.system("python manage.py collectstatic --no-input")

DJANGO_SUPERUSER_USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME')
DJANGO_SUPERUSER_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')

# Create superuser
try:
    os.system(f"python manage.py createsuperuser \
        --noinput \
        --username {DJANGO_SUPERUSER_USERNAME} \
        --email {DJANGO_SUPERUSER_EMAIL}")

except CommandError:
    print("The superuser was not created")

workers = multiprocessing.cpu_count() * 2 + 1
os.system("gunicorn insurer.wsgi:application \
          --bind 0.0.0.0:8000 \
          --workers={} \
          --config {}".format(workers, './gunicorn.conf.py'))

