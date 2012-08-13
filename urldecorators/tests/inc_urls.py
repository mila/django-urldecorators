
from urldecorators.defaults import * # Legacy import location
from urldecorators.tests.urls import decorator1, decorator2, Middleware1, Middleware2

from urldecorators.tests import views


urlpatterns = patterns('urldecorators.tests.views',
    # Url
    url(r'^$', 'sample_view'),
    # Url with args
    url(r'^args/(\d+)/(\d+)/$', 'sample_view'),
    # Url with kwargs
    url(r'^kwargs/(?P<inc_arg1>\d+)/(?P<inc_arg2>\d+)/$', 'sample_view'),
    # Include
    url(r'^inc/', include("urldecorators.tests.inc_inc_urls")),
    # Url with decorators
    url(r'^decorators/$', 'sample_view',
        decorators=[decorator1, decorator2]
    ),
    # Include with decorators
    url(r'^decorators/inc/',
        include("urldecorators.tests.inc_inc_urls"),
        decorators=[decorator1, decorator2]
    ),
    # Url with middleware
    url(r'^middleware/$', 'sample_view',
        middleware_classes=[Middleware1, Middleware2]
    ),
    # Include with middleware
    url(r'^middleware/inc/',
        include("urldecorators.tests.inc_inc_urls"),
        middleware_classes=[Middleware1, Middleware2]
    ),
)

urlpatterns += patterns('urldecorators.tests.views',
    url(r'^func/$', views.sample_view),
    url(r'^class/$', views.class_view),
    url(r'^method/$', views.method_view),
    url(r'^func-str/$', 'sample_view'),
    url(r'^class-str/$', 'class_view'),
    url(r'^method-str/$', 'method_view'),
)

if views.generic_view:
    urlpatterns += patterns('urldecorators.tests.views',
        url(r'^generic/$', views.generic_view),
        url(r'^generic-str/$', 'generic_view'),
    )
