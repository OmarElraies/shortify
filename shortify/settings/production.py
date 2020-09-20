from .base import *

import os


# ALLOWED_HOSTS += (
#     '3.23.98.11','3.23.98.11:8000','3.23.98.11:8080'
# )

ALLOWED_HOSTS = ['18.223.44.253']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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