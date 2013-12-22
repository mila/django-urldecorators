
from urldecorators import patterns, url, include
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^private/$', include('example.private.urls'),
        decorators=['django.contrib.auth.decorators.login_required']),
    url(r'^cached/$', include('example.cached.urls'),
        middleware_classes=['django.middleware.cache.CacheMiddleware']),
)

# Nothing special about following urlpatterns.
urlpatterns += patterns('',
    url('^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name="logout"),
)
