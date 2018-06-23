"""Stage settings."""

import os
import django_heroku
import dj_database_url

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['.herokuapp.com']

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]


# Application definition

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

# SSL/HTTPS
# https://docs.djangoproject.com/en/1.11/topics/security/#ssl-https

SECURE_SSL_REDIRECT = True


# Sentry

SENTRY_DSN = os.environ.get('SENTRY_DSN')

RAVEN_CONFIG = {
    'site': os.environ.get('HEROKU_APP_NAME')
}


# Database

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Static files (Whitenoise)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

WHITENOISE_STATIC_PREFIX = STATIC_URL

STATIC_URL = os.environ.get('DJANGO_STATIC_HOST', STATIC_URL)

django_heroku.settings(locals())
