"""
Minimal settings for running tests.

Allows to run test suite without any project configured:

    $ django-admin.py test --settings=urldecorators.tests.settings

"""

# Django 1.1 and 1.0
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = ':memory:'

# Django 1.2 up
DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME
    }
}

# Must be configured even thought it is not actually needed
ROOT_URLCONF = None


INSTALLED_APPS = (
    'urldecorators',
)
