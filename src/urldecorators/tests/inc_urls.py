
from urldecorators.defaults import *
from urldecorators.tests.urls import decorator1, decorator2, Middleware1, Middleware2


urlpatterns = patterns('urldecorators.tests.views',
    url(r'^$', 'sample_view'),
    url(r'^args/(\d+)/(\d+)/$', 'sample_view'),
    url(r'^kwargs/(?P<inc_arg1>\d+)/(?P<inc_arg2>\d+)/$', 'sample_view'),
    url(r'^inc/(?P<inc_arg1>\d+)/(?P<inc_arg2>\d+)/', include("urldecorators.tests.inc_inc_urls")),
    url(r'^class/$', 'class_view'),
    
    url(r'^decorators/$', 'sample_view', decorators=[decorator1, decorator2]),
    url(r'^decorators/(?P<inc_arg1>\d+)/(?P<inc_arg2>\d+)/', include("urldecorators.tests.inc_inc_urls"), decorators=[decorator1, decorator2]),    
    url(r'^middleware/$', 'sample_view', middleware_classes=[Middleware1, Middleware2]),
    url(r'^middleware/(?P<inc_arg1>\d+)/(?P<inc_arg2>\d+)/', include("urldecorators.tests.inc_inc_urls"), middleware_classes=[Middleware1, Middleware2]),    
)



