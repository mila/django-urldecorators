Django-urldecorators is a reusable Django application which allows apply
view decorators and middleware components based on requested URL.

The application is compatible with Django versions from 1.0 to 1.4.


Installation and usage
======================

1) Run `python setup.py install` or add `urldecorators` directory to
   your `PYTHONPATH` (or use pip or easy_install).

2) In `urls.py` file replace `from django.conf.urls import *`
   by `from urldecorators import *`

3) Pass a list of decorators and/or middleware_classes as an argument
   to the `url` function.

Example urls.py file: ::

    from urldecorators import *

    urlpatterns = patterns('',
        url(r'^private/$', include('example.private.urls'),
            decorators=['django.contrib.auth.decorators.login_required']),
        url(r'^articles/$', include('example.articles.urls'),
            middleware_classes=['django.middleware.cache.CacheMiddleware']),
    )


For the example configuration and usage see the example project included
in the repository. It can be run using `django-admin.py` utility from the
repository root: ::

    $ django-admin.py syncdb --settings=example.settings --pythonpath=`pwd`
    $ django-admin.py runserver --settings=example.settings --pythonpath=`pwd`


Testing
=======

Application tests can be simply run using `django-admin.py` utility: ::

    $ django-admin.py test --settings=urldecorators.tests.settings --pythonpath=`pwd`

Alternatively you can include `urldecorators` in `INSTALLED_APPS` so that all
the tests will be run automatically with your project test suite.
