"""
Minimal settings for running tests.

Allows to run test suite without any project configured:

    $ django-admin.py test --settings=urldecorators.tests.settings

"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

ROOT_URLCONF = 'urldecorators.tests.urls'


INSTALLED_APPS = (
    'urldecorators',
)

SECRET_KEY = 'The SECRET_KEY setting must not be empty.'

# Prevents warning in Django 1.7
MIDDLEWARE_CLASSES = []