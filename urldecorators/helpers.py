
from django.core.exceptions import ImproperlyConfigured
from django.utils.decorators import decorator_from_middleware
from django.utils import six

from functools import update_wrapper, WRAPPER_ASSIGNMENTS


def import_if_string(path):
    if not isinstance(path, six.string_types):
        return path
    try:
        dot = path.rindex('.')
    except ValueError:
        raise ImproperlyConfigured('%s isn\'t a valid module' % path)
    mod_name, obj_name = path[:dot], path[dot+1:]
    try:
        mod = __import__(mod_name, {}, {}, [''])
    except ImportError as e:
        raise ImproperlyConfigured('Error importing module %s: "%s"'
                                    % (mod_name, e))
    try:
        obj = getattr(mod, obj_name)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define "%s"'
                                   % (mod_name, obj_name))
    return obj


def get_decorator_tuple(decorators, middleware_classes):
    middleware_classes = [decorator_from_middleware(import_if_string(middleware_class))
                          for middleware_class in middleware_classes or []]
    decorators = [import_if_string(decorator) for decorator in decorators or []]
    return tuple(middleware_classes + decorators)[::-1]


def func_from_callable(callable):
    """
    Converts callable to standard function
    """
    assigned = tuple(a for a in WRAPPER_ASSIGNMENTS if hasattr(callable, a))
    def func(*args, **kwargs):
        return callable(*args, **kwargs)
    update_wrapper(func, callable, assigned=assigned)
    return func
