import environ
from rest_framework import permissions

env = environ.Env()

SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='not secret)')

DEBUG = env.str('DJANGO_DEBUG', default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

ALLOWED_HOSTS = env.str('DJANGO_ALLOWED_HOSTS', default='*')

if DEBUG:
    API_PERMISSION = permissions.AllowAny
else:
    API_PERMISSION = permissions.IsAuthenticated

INTERNAL_IPS = [
    '127.0.0.1',
]
