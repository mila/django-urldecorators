from urldecorators.defaults import *

urlpatterns = patterns('',                       
    url(r'^private/$', include('testproject.private.urls'), 
        decorators=['django.contrib.auth.decorators.login_required']),
    url(r'^articles/$', include('testproject.articles.urls'),
        middleware_classes=['django.middleware.cache.CacheMiddleware']),
)

urlpatterns += patterns('',
     ("^$", 'django.views.generic.simple.direct_to_template',  
            {'template': 'index.html'}),
    (r'^login/$', 'django.contrib.auth.views.login', 
            {'template_name': 'login.html'}),
)

from django.contrib import admin
admin.autodiscover()

if hasattr(admin.site, "urls"):
    urlpatterns += patterns('',
        (r'^admin/', include(admin.site.urls)),
    )
else:
    urlpatterns += patterns('',
        (r'^admin/(.*)', admin.site.root),
    )
    