from .base import *

import os


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += (
)

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shortifydb',
        'USER': 'shortifyuser',
        'PASSWORD': 'omar1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}