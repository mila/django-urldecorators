from urldecorators.defaults import *

urlpatterns = patterns('',                       
    url(r'^private/$', include('testproject.private.urls'), 
        decorators=['django.contrib.auth.decorators.login_required']),
    url(r'^cached/$', include('testproject.cached.urls'),
        middleware_classes=['django.middleware.cache.CacheMiddleware']),
)

urlpatterns += patterns('',
    url("^$", 'django.views.generic.simple.direct_to_template',  
            {'template': 'index.html'}, name="home"),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
)   
