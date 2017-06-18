
from urldecorators import url, include
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^private/', include('example.private.urls'),
        decorators=['django.contrib.auth.decorators.login_required']),
    url(r'^cached/', include('example.cached.urls'),
        middleware_classes=['django.middleware.cache.CacheMiddleware']),
]

# Nothing special about following urlpatterns.
urlpatterns += [
    url('^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^accounts/login/$', auth_views.login, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, name="logout"),
]
