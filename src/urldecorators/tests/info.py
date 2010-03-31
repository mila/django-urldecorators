
from django.conf.urls.defaults import url, include

# http://code.djangoproject.com/changeset/9728
try:
    url('', include([])).url_patterns
except TypeError:
    include_on_an_iterable_of_patterns = False
else:
    include_on_an_iterable_of_patterns = True
    
    
# http://code.djangoproject.com/changeset/11250
try:
    include("some.urls", namespace="foo", app_name="bar")
except TypeError:    
    namespacing_named_urls = False
else:
    namespacing_named_urls = True
    

