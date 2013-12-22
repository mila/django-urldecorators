
try:
    from functools import update_wrapper
except ImportError:
    from django.utils.functional import update_wrapper

from urldecorators import patterns, url, include


def decorator1(func):
    def wrapper(request, *args, **kwargs):
        args += ("decorator 1 applied",)
        return func(request, *args, **kwargs)
    update_wrapper(wrapper, func)
    return wrapper

def decorator2(func):
    def wrapper(request, *args, **kwargs):
        args += ("decorator 2 applied",)
        return func(request, *args, **kwargs)
    update_wrapper(wrapper, func)
    return wrapper

class Middleware1(object):
    def process_view(self, request, func, args, kwargs):
        args += ("middleware 1 applied",)
        return func(request, *args, **kwargs)

class Middleware2(object):
    def process_view(self, request, func, args, kwargs):
        args += ("middleware 2 applied",)
        return func(request, *args, **kwargs)


# Basic
urlpatterns = patterns('urldecorators.tests.views',
    # Url
    url(r'^$', 'sample_view'),
    # Url with args
    url(r'^args/(\d+)/(\d+)/$', 'sample_view'),
    # Url with kwargs
    url(r'^kwargs/(?P<arg1>\d+)/(?P<arg2>\d+)/$', 'sample_view'),
    # Include
    url(r'^inc/', include("urldecorators.tests.inc_urls")),
    # Include with kwargs
    url(r'^kwargs/(?P<arg1>\d+)/(?P<arg2>\d+)/inc/',
        include("urldecorators.tests.inc_urls")),
)

# Decorators
urlpatterns += patterns('urldecorators.tests.views',
    # Url
    url(r'^decorators/$', 'sample_view',
        decorators=[decorator1, decorator2]
    ),
    # Url with args
    url(r'^decorators/args/(\d+)/(\d+)/$', 'sample_view',
        decorators=[decorator1, decorator2]
    ),
    # Url with kwargs
    url(r'^decorators/kwargs/(?P<arg1>\d+)/(?P<arg2>\d+)/$', 'sample_view',
        decorators=[decorator1, decorator2]
    ),
    # Include
    url(r'^decorators/inc/',
        include("urldecorators.tests.inc_urls"),
        decorators=[decorator1, decorator2]
    ),
    # Include with kwargs
    url(r'^decorators/kwargs/(?P<arg1>\d+)/(?P<arg2>\d+)/inc/',
        include("urldecorators.tests.inc_urls"),
        decorators=[decorator1, decorator2]
    ),
)

# Middleware
urlpatterns += patterns('urldecorators.tests.views',
    # Url
    url(r'^middleware/$', 'sample_view',
        middleware_classes=[Middleware1, Middleware2]
    ),
    # Url with args
    url(r'^middleware/args/(\d+)/(\d+)/$', 'sample_view',
        middleware_classes=[Middleware1, Middleware2]
    ),
    # Url with kwargs
    url(r'^middleware/kwargs/(?P<arg1>\d+)/(?P<arg2>\d+)/$', 'sample_view',
        middleware_classes=[Middleware1, Middleware2]
    ),
    # Include
    url(r'^middleware/inc/',
        include("urldecorators.tests.inc_urls"),
        middleware_classes=[Middleware1, Middleware2]),
    # Include with kwargs
    url(r'^middleware/kwargs/(?P<arg1>\d+)/(?P<arg2>\d+)/inc/',
        include("urldecorators.tests.inc_urls"),
        middleware_classes=[Middleware1, Middleware2]),
)

# Misc
urlpatterns += patterns('urldecorators.tests.views',
    # Url with middleware and decorators combination
    url(r'^middleware-and-decorators/$', 'sample_view',
        middleware_classes=[Middleware1, Middleware2],
        decorators=[decorator1, decorator2]
    ),
    # Include with middleware and decorators combination
    url(r'^middleware-and-decorators/inc/',
        include("urldecorators.tests.inc_urls"),
        middleware_classes=[Middleware1, Middleware2],
        decorators=[decorator1, decorator2]
    ),
    # Decorators declared as a string
    url(r'^string/decorators/$', 'sample_view',
        decorators=["urldecorators.tests.urls.decorator1",
                    u"urldecorators.tests.urls.decorator2"]
    ),
    # Middleware declared as a string
    url(r'^string/middleware/$', 'sample_view',
        middleware_classes=["urldecorators.tests.urls.Middleware1",
                            u"urldecorators.tests.urls.Middleware2"]
    ),
)

# Include iterable in urlpatterns.
attr_urls = patterns('urldecorators.tests.views',
    url(r'^$', 'sample_view'),
    url(r'^decorators/$', 'sample_view',
        decorators=[decorator1, decorator2]),
    url(r'^middleware/$', 'sample_view',
        middleware_classes=[Middleware1, Middleware2]),
)
urlpatterns += patterns('urldecorators.tests.views',
    # Test urls as property instead of a module
    url(r'^attr/inc/', include(attr_urls)),
    url(r'^attr/decorators/', include(attr_urls),
        decorators=[decorator1, decorator2]
    ),
    url(r'^attr/middleware/', include(attr_urls),
        middleware_classes=[Middleware1, Middleware2]
    ),
)

# Namespaced urls.
urlpatterns += patterns('urldecorators.tests.views',
    url(r'^namespace/decorators/',
        include("urldecorators.tests.inc_urls", namespace='foo', app_name='bar'),
        decorators=[decorator1, decorator2]
    ),
    url(r'^namespace/middleware/',
        include("urldecorators.tests.inc_urls", namespace='foo', app_name='bar'),
        middleware_classes=[Middleware1, Middleware2]
    ),
)
