import environ
from rest_framework import permissions

env = environ.Env()


SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env.str('POSTGRES_NAME'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

if DEBUG:
    API_PERMISSION = permissions.AllowAny
else:
    API_PERMISSION = permissions.IsAuthenticated
