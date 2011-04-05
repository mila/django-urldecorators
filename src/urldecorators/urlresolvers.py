
import types
from django.core import urlresolvers as django_urlresolvers
from django.utils.functional import curry

class DecoratorMixin(object):
    """
    Mixin class to return decorated views from RegexURLPattern/RegexURLResolver
    """
    
    def __init__(self, *args, **kwargs):
        super(DecoratorMixin, self).__init__(*args, **kwargs)
        self.decorators = []
    
    def resolve(self, path):
        match = super(DecoratorMixin, self).resolve(path)
        if not match:
            return match
        try:
            # In Django 1.3 match is an instance of ResolverMatch class
            match.func = self.apply_decorators(match.func)
        except AttributeError:
            # Before Django 1.3 match is a tuple 
            match = self.apply_decorators(match[0]), match[1], match[2]
        return match
    
    def apply_decorators(self, callback):
        if not isinstance(callback, types.FunctionType):
            callback = curry(callback) # Some decorators do not work with class views
        for decorator in self.decorators:
            callback = decorator(callback)
        return callback
    
class RegexURLPattern(DecoratorMixin, django_urlresolvers.RegexURLPattern):
    pass

class RegexURLResolver(DecoratorMixin, django_urlresolvers.RegexURLResolver):
    pass
    

