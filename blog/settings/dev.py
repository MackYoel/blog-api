"""Local settings for development."""

from .base import *  # noqa

ALLOWED_HOSTS = ['*']


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# Application definition

INSTALLED_APPS += [
    'debug_toolbar',
]


# Internal IPs

INTERNAL_IPS = [
    '127.0.0.1',
]


# Rest framework

USE_REST_FRAMEWORK_FORMS = os.environ.get('USE_REST_FRAMEWORK_FORMS', True)

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += (
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication'
)

if not USE_REST_FRAMEWORK_FORMS:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'utils.api.BrowsableAPIRendererWithoutForms',
    )
