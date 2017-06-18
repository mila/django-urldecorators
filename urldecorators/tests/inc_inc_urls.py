
from django.conf.urls import url

from urldecorators.tests import views


urlpatterns = [
    url(r'^$', views.sample_view),
    url(r'^args/(\d+)/(\d+)/$', views.sample_view),
    url(r'^kwargs/(?P<inc_inc_arg1>\d+)/(?P<inc_inc_arg2>\d+)/$', views.sample_view),
]
