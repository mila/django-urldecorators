
from django.template import defaulttags

def fix():
    if "csrf_token" not in defaulttags.register.tags:
        def csrf_token():
            # This no-op tag exists to allow 1.1.X code to be compatible with Django 1.2
            return ""
        defaulttags.register.simple_tag(csrf_token)