import os

DEBUG = True

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'test.db')

ROOT_URLCONF = 'testproject.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    
    'urldecorators',
)

LOGIN_URL = '/login/'
