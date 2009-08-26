
from django.test import TestCase
from urldecorators.tests.info import include_on_an_iterable_of_patterns, namespacing_named_urls


class ResolveTestCase(TestCase):
    
    urls = "urldecorators.tests.urls"
    
    def test_base_pattern(self):        
        r = self.client.get("/")
        self.assertEqual((r.args, r.kwargs), ((), {}))
        r = self.client.get("/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (("1", "2"), {}))
        r = self.client.get("/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), ((), {"arg1":"1", "arg2":"2"}))
    
    def test_base_resolver(self):
        r = self.client.get("/inc/1/2/")
        self.assertEqual((r.args, r.kwargs), ((), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/inc/1/2/args/3/4/")
        self.assertEqual((r.args, r.kwargs), (("3", "4"), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/inc/1/2/kwargs/3/4/")
        self.assertEqual((r.args, r.kwargs), ((), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))
     
    def test_pattern_with_decorators(self):
        r = self.client.get("/decorators/")
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {}))
        
    def test_resolver_with_decorators(self):
        r = self.client.get("/decorators/1/2/")
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/decorators/1/2/args/3/4/")
        self.assertEqual((r.args, r.kwargs), (("3", "4", "decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/decorators/1/2/kwargs/3/4/")
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))
        
    def test_include_in_resolver_with_decorators(self):
        r = self.client.get("/decorators/1/2/inc/3/4/")
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))
        r = self.client.get("/decorators/1/2/inc/3/4/args/5/6/")
        self.assertEqual((r.args, r.kwargs), (("5", "6", "decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))
        r = self.client.get("/decorators/1/2/inc/3/4/kwargs/5/6/")
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4", "inc_inc_arg1":"5", "inc_inc_arg2":"6"}))
        
    def test_pattern_with_middleware(self):
        r = self.client.get("/middleware/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {}))
        
    def test_resolver_with_middleware(self):
        r = self.client.get("/middleware/1/2/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/middleware/1/2/args/3/4/")
        self.assertEqual((r.args, r.kwargs), (("3", "4", "middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/middleware/1/2/kwargs/3/4/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))

    def test_include_in_resover_with_middleware(self):
        r = self.client.get("/middleware/1/2/inc/3/4/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))
        r = self.client.get("/middleware/1/2/inc/3/4/args/5/6/")
        self.assertEqual((r.args, r.kwargs), (("5", "6", "middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))
        r = self.client.get("/middleware/1/2/inc/3/4/kwargs/5/6/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4", "inc_inc_arg1":"5", "inc_inc_arg2":"6"}))
        
    def test_middleware_decorators_order(self):
        r = self.client.get("/middleware-and-decorators/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied", "decorator 1 applied", "decorator 2 applied"), {}))
        r = self.client.get("/middleware-and-decorators/inc/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied", "decorator 1 applied", "decorator 2 applied"), {}))
        
    def test_resolver_in_resolver_both_with_decorators_or_middleware(self):
        r = self.client.get("/decorators/1/2/middleware/3/4/")        
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied", "middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))
        r = self.client.get("/middleware/1/2/decorators/3/4/")        
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied", "decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}))        
        
    def test_pattern_in_resolver_both_with_decorators_or_middleware(self):
        r = self.client.get("/decorators/1/2/middleware/")        
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied", "middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/middleware/1/2/decorators/")        
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied", "decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2"}))
        
    def test_resolver_with_class_view(self):
        r = self.client.get("/decorators/1/2/class/")
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {"arg1":"1", "arg2":"2"}))
        r = self.client.get("/middleware/1/2/class/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {"arg1":"1", "arg2":"2"}))
        
    def test_decorators_defined_as_string(self):
        r = self.client.get("/string-decorators/")
        self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {}))
        
    def test_middleware_defined_as_string(self):
        r = self.client.get("/string-middleware/")
        self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {}))
    
    if include_on_an_iterable_of_patterns:
        def test_decorators_and_middleware_in_resolver_with_attr_as_urlconf(self):            
            r = self.client.get("/inc-attr/decorators/")
            self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {}))
            r = self.client.get("/inc-attr/middleware/")
            self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {}))
            
        def test_resolver_with_attr_as_urlconf_and_decorators_or_middleware(self):
            r = self.client.get("/inc-attr-decorators/")
            self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {}))
            r = self.client.get("/inc-attr-middleware/")
            self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {}))
            
    if namespacing_named_urls:        
        def test_resolver_with_app_namespace_and_decorators_or_middleware(self):            
            r = self.client.get("/namespace-decorators/")
            self.assertEqual((r.args, r.kwargs), (("decorator 1 applied", "decorator 2 applied"), {}))
            r = self.client.get("/namespace-middleware/")
            self.assertEqual((r.args, r.kwargs), (("middleware 1 applied", "middleware 2 applied"), {}))
          

