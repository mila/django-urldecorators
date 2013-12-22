
from django.http import HttpResponse
from django.views.generic.base import View


def sample_view(request, *args, **kwargs):
    response = HttpResponse("ok")
    response.args = args
    response.kwargs = kwargs
    return response


class ClassView(object):
    def __call__(self, request, *args, **kwargs):
        return sample_view(request, *args, **kwargs)
class_view = ClassView()


class MethodView(object):
    def method(self, request, *args, **kwargs):
        return sample_view(request, *args, **kwargs)
method_view = MethodView().method


class GenericView(View):
    def get(self, request, *args, **kwargs):
        return sample_view(request, *args, **kwargs)
generic_view = GenericView.as_view()
