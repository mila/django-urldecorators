
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
        callback, args, kwargs = match
        callback = self.apply_decorators(callback)
        return callback, args, kwargs
        
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
    

