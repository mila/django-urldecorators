
import os


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.abspath('%s/../../example.db' % __file__),
    }
}

ROOT_URLCONF = 'example.urls'

TEMPLATE_DIRS = (
    os.path.abspath('%s/../templates/' % __file__),
)

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes', # Required for auth
    'django.contrib.admin',        # Required by django.contrib.auth tests
    'django.contrib.sites',        # Required by django.contrib.auth tests

    'urldecorators',               # Optional, only for Django test runner
)

SECRET_KEY = 'The SECRET_KEY setting must not be empty.'
