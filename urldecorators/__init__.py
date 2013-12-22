
from django.conf import urls
from django.core.exceptions import ImproperlyConfigured

from urldecorators.urlresolvers import RegexURLPattern, RegexURLResolver
from urldecorators.helpers import get_decorator_tuple


__all__ = ['include', 'patterns', 'url']

include = urls.include
patterns = urls.patterns


def url(regex, view, kwargs=None, name=None, prefix='', decorators=None,
        middleware_classes=None):
    """
    Extended `django.conf.urls.url` with support for view decorators
    and middleware_classes

    Using this function instead of Django defaults you can:
     - Activate middleware component for only a subset of your urls/views
     - Apply view decorator for multiple views in one place

    Example urls.py file:

        from urldecorators import patterns, url, include

        urlpatterns = patterns('',
            url(r'^private/$', include('example.private.urls'),
                decorators=['django.contrib.auth.decorators.login_required']),
            url(r'^articles/$', include('example.articles.urls'),
                middleware_classes=['django.middleware.cache.CacheMiddleware']),
        )

    """
    if not (decorators or middleware_classes):
        return urls.url(regex, view, kwargs, name, prefix)
    r = _url(regex, view, kwargs, name, prefix)
    r.decorators = get_decorator_tuple(decorators, middleware_classes)
    return r


def _url(regex, view, kwargs=None, name=None, prefix='', decorators=None,
         pattern=RegexURLPattern, resolver=RegexURLResolver):
    """
    Modified `django.conf.urls.url` with allows to specify custom
    RegexURLPattern and RegexURLResolver classes.
    """
    if isinstance(view, (list,tuple)):
        # For include(...) processing.
        return resolver(regex, view[0], kwargs, *view[1:])
    else:
        if isinstance(view, basestring):
            if not view:
                raise ImproperlyConfigured('Empty URL pattern view name not permitted (for pattern %r)' % regex)
            if prefix:
                view = prefix + '.' + view
        return pattern(regex, view, kwargs, name)
