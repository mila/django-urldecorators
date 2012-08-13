
import os


DEBUG = False

# Django 1.1 and 1.0
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = os.path.abspath('%s/../../example.db' % __file__)

# Django 1.2 up
DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME
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
