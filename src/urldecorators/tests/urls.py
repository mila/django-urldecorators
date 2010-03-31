
from urldecorators.defaults import *
from urldecorators.tests.info import include_on_an_iterable_of_patterns, namespacing_named_urls

def decorator1(func):
    def wrapped(request, *args, **kwargs):
        args += ("decorator 1 applied",)
        return func(request, *args, **kwargs)    
    return wrapped

def decorator2(func):
    def wrapped(request, *args, **kwargs):
        args += ("decorator 2 applied",)
        return func(request, *args, **kwargs)    
    return wrapped

class Middleware1(object):    
    def process_view(self, request, func, args, kwargs):
        args += ("middleware 1 applied",)
        return func(request, *args, **kwargs)

class Middleware2(object):    
    def process_view(self, request, func, args, kwargs):
        args += ("middleware 2 applied",)
        return func(request, *args, **kwargs)    


attr_urls = patterns('urldecorators.tests.views',    
    url(r'^$', 'sample_view'),
    url(r'^decorators/$', 'sample_view', decorators=[decorator1, decorator2]),    
    url(r'^middleware/$', 'sample_view', middleware_classes=[Middleware1, Middleware2]),
) 

urlpatterns = patterns('urldecorators.tests.views',
    # Test defaults 
    url(r'^$', 'sample_view'),
    url(r'^args/(\d+)/(\d+)/$', 'sample_view'),
    url(r'^kwargs/(?P<arg1>\d+)/(?P<arg2>\d+)/$', 'sample_view'),        
    url(r'^inc/(?P<arg1>\d+)/(?P<arg2>\d+)/', include("urldecorators.tests.inc_urls")),    
    # Test decorators
    url(r'^decorators/$', 'sample_view', decorators=[decorator1, decorator2]),
    url(r'^decorators/(?P<arg1>\d+)/(?P<arg2>\d+)/', include("urldecorators.tests.inc_urls"), decorators=[decorator1, decorator2]),
    # Test middleware    
    url(r'^middleware/$', 'sample_view', middleware_classes=[Middleware1, Middleware2]),
    url(r'^middleware/(?P<arg1>\d+)/(?P<arg2>\d+)/', include("urldecorators.tests.inc_urls"), middleware_classes=[Middleware1, Middleware2]),
    # Test order of decorators and middleware  
    url(r'^middleware-and-decorators/$', 'sample_view', middleware_classes=[Middleware1, Middleware2], decorators=[decorator1, decorator2]),
    url(r'^middleware-and-decorators/inc/', include("urldecorators.tests.inc_urls"), middleware_classes=[Middleware1, Middleware2], decorators=[decorator1, decorator2]),
    # Test decorators and middleware defined as strings
    url(r'^string-decorators/$', 'sample_view', decorators=["urldecorators.tests.urls.decorator1", u"urldecorators.tests.urls.decorator2"]),
    url(r'^string-middleware/$', 'sample_view', middleware_classes=["urldecorators.tests.urls.Middleware1", u"urldecorators.tests.urls.Middleware2"]),
    
)

if include_on_an_iterable_of_patterns:
    urlpatterns += patterns('urldecorators.tests.views',
        # Test urls as property instead of a module
        url(r'^inc-attr/', include(attr_urls)),
        url(r'^inc-attr-decorators/', include(attr_urls), decorators=[decorator1, decorator2]),
        url(r'^inc-attr-middleware/', include(attr_urls), middleware_classes=[Middleware1, Middleware2]),
    )

if namespacing_named_urls:
    urlpatterns += patterns('urldecorators.tests.views',
        # Test app namespaces                
        url(r'^namespace-decorators/', include("urldecorators.tests.inc_urls", namespace='foo', app_name='bar'), decorators=[decorator1, decorator2]),
        url(r'^namespace-middleware/', include("urldecorators.tests.inc_urls", namespace='foo', app_name='bar'), middleware_classes=[Middleware1, Middleware2]),        
    )
