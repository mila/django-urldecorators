
from django.http import HttpResponse

def sample_view(request, *args, **kwargs):    
    response = HttpResponse("ok")
    response.args = args 
    response.kwargs = kwargs 
    return response

class ClassView(object):    
    def __call__(self, request, *args, **kwargs):    
        response = HttpResponse("ok")
        response.args = args 
        response.kwargs = kwargs 
        return response    
class_view = ClassView()

