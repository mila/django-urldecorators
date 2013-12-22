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

# Must be configured even thought it is not actually needed
ROOT_URLCONF = None


INSTALLED_APPS = (
    'urldecorators',
)

SECRET_KEY = 'The SECRET_KEY setting must not be empty.'
