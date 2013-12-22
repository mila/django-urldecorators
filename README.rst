Django-urldecorators is a reusable Django application which allows apply
view decorators and middleware components based on a requested URL.

This library is compatible with Django 1.4 and later. If you need to use
older Django versions (which receive no security updates or bugfixes) you
can install 0.4 version of django-urldecorators.


Installation and usage
======================

1) Run `python setup.py install` or add the `urldecorators` module to
   your `PYTHONPATH` (or use pip or easy_install).

2) In `urls.py` file replace `from django.conf.urls import *`
   by `from urldecorators import *`

3) Pass a list of decorators and/or middleware_classes as an argument
   to the `url` function.

Example urls.py file: ::

    from urldecorators import patterns, url, include

    urlpatterns = patterns('',
        url(r'^private/$', include('example.private.urls'),
            decorators=['django.contrib.auth.decorators.login_required']),
        url(r'^articles/$', include('example.articles.urls'),
            middleware_classes=['django.middleware.cache.CacheMiddleware']),
    )


For the example configuration and usage see the example project included
in the repository. It can be run using `django-admin.py` utility from the
repository root: ::

    $ django-admin.py syncdb --settings=example.settings --pythonpath=$PWD
    $ django-admin.py runserver --settings=example.settings --pythonpath=$PWD


Testing
=======

Application tests can be simply run using `django-admin.py` utility: ::

    $ django-admin.py test --settings=urldecorators.tests.settings --pythonpath=$PWD
