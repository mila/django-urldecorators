
from django.conf.urls.defaults import *

urlpatterns = patterns('urldecorators.tests.views',
    url(r'^$', 'sample_view'),
    url(r'^args/(\d+)/(\d+)/$', 'sample_view'),
    url(r'^kwargs/(?P<inc_inc_arg1>\d+)/(?P<inc_inc_arg2>\d+)/$', 'sample_view'),
)
