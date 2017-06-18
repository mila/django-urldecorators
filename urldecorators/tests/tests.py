
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from urldecorators import url
from urldecorators.tests import views


__all__ = ["ResolverTestCase", "ConfigurationTestCase", "ViewTypesTestCase"]


class ResolverTestCase(TestCase):

    def test_view_is_resolved(self):
        r = self.client.get("/")
        self.assertEqual((r.args, r.kwargs),((), {}))

    def test_args_are_parsed(self):
        r = self.client.get("/args/1/2/")
        self.assertEqual((r.args, r.kwargs),(("1", "2"), {}))

    def test_kwargs_are_parsed(self):
        r = self.client.get("/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), ((), {"arg1":"1", "arg2":"2"}))

    def test_included_view_is_resolved(self):
        r = self.client.get("/inc/")
        self.assertEqual((r.args, r.kwargs), ((), {}))

    def test_included_args_are_parsed(self):
        r = self.client.get("/inc/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (("1", "2"), {}))

    def test_included_kwargs_are_parsed(self):
        r = self.client.get("/inc/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            (), {"inc_arg1":"1", "inc_arg2":"2"}
        ))

    def test_kwargs_are_merged(self):
        r = self.client.get("/kwargs/1/2/inc/kwargs/3/4/")
        self.assertEqual((r.args, r.kwargs), (
            (), {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}
        ))

    def test_decorators_are_applied_to_url(self):
        r = self.client.get("/decorators/")
        self.assertEqual(
            (r.args, r.kwargs),
            (("decorator 1 applied", "decorator 2 applied"), {})
        )

    def test_args_are_parsed_for_decorated_url(self):
        r = self.client.get("/decorators/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("1", "2", "decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_kwargs_are_parsed_for_decorated_url(self):
        r = self.client.get("/decorators/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"),
            {"arg1":"1", "arg2":"2"}
        ))

    def test_decorators_are_applied_to_include(self):
        r = self.client.get("/decorators/inc/")
        self.assertEqual((r.args, r.kwargs),(
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_args_are_parsed_for_decorated_include(self):
        r = self.client.get("/decorators/inc/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("1", "2", "decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_kwargs_are_parsed_for_decorated_include(self):
        r = self.client.get("/decorators/inc/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"),
            {"inc_arg1":"1", "inc_arg2":"2"}
        ))

    def test_kwargs_are_merged_for_decorated_include(self):
        r = self.client.get("/decorators/kwargs/1/2/inc/kwargs/3/4/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"),
            {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}
        ))

    def test_decorators_are_applied_to_include_in_decorated_include(self):
        r = self.client.get("/decorators/inc/inc/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_args_are_parsed_for_include_in_decorated_include(self):
        r = self.client.get("/decorators/inc/inc/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("1", "2", "decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_kwargs_are_parsed_for_include_in_decorated_include(self):
        r = self.client.get("/decorators/inc/inc/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"),
            {"inc_inc_arg1":"1", "inc_inc_arg2":"2"}
        ))

    def test_middleware_is_applied_to_url(self):
        r = self.client.get("/middleware/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_args_are_parsed_for_url_w_middleware(self):
        r = self.client.get("/middleware/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("1", "2", "middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_kwargs_are_parsed_for_url_w_middleware(self):
        r = self.client.get("/middleware/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"),
            {"arg1":"1", "arg2":"2"}
        ))

    def test_middleware_is_applied_to_include(self):
        r = self.client.get("/middleware/inc/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_args_are_parsed_for_include_w_middleware(self):
        r = self.client.get("/middleware/inc/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("1", "2", "middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_kwargs_are_parsed_for_include_w_middleware(self):
        r = self.client.get("/middleware/inc/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"),
            {"inc_arg1":"1", "inc_arg2":"2"}
        ))

    def test_kwargs_are_merged_for_include_w_middleware(self):
        r = self.client.get("/middleware/kwargs/1/2/inc/kwargs/3/4/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"),
            {"arg1":"1", "arg2":"2", "inc_arg1":"3", "inc_arg2":"4"}
        ))

    def test_middleware_is_applied_to_include_in_include_w_middleware(self):
        r = self.client.get("/middleware/inc/inc/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_args_are_parsed_for_include_in_include_w_middleware(self):
        r = self.client.get("/middleware/inc/inc/args/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("1", "2", "middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_kwargs_are_parsed_for_include_in_include_w_middleware(self):
        r = self.client.get("/middleware/inc/inc/kwargs/1/2/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"),
            {"inc_inc_arg1":"1", "inc_inc_arg2":"2"}
        ))

    def test_middleware_is_appliled_before_decorators_to_url(self):
        r = self.client.get("/middleware-and-decorators/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied",
             "decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_is_applied_before_decorators_to_include(self):
        r = self.client.get("/middleware-and-decorators/inc/")
        self.assertEqual( (r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied",
             "decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_include_w_middleware_in_decorated_include(self):
        r = self.client.get("/decorators/inc/middleware/inc/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied",
             "middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_decorated_include_in_include_w_middleware(self):
        r = self.client.get("/middleware/inc/decorators/inc/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied",
             "decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_url_w_middleware_in_decorated_include(self):
        r = self.client.get("/decorators/inc/middleware/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied",
             "middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_decorated_url_in_include_w_middleware(self):
        r = self.client.get("/middleware/inc/decorators/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied",
             "decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_decorators_work_with_namespaced_urls(self):
        r = self.client.get("/namespace/decorators/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_works_with_namespaced_urls(self):
        r = self.client.get("/namespace/middleware/")
        self.assertEqual((r.args, r.kwargs), (
        ("middleware 1 applied", "middleware 2 applied"), {}
    ))


class ConfigurationTestCase(TestCase):

    def test_decorators_can_be_declared_as_string(self):
        r = self.client.get("/string/decorators/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_can_be_declared_as_string(self):
        r = self.client.get("/string/middleware/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_empty_string_as_view_name_raises(self):
        def func():
            urlpatterns = [
                url(r'^$', '', decorators=["urldecorators.tests.urls.decorator1"]),
            ]
        self.assertRaises(ImproperlyConfigured, func)

    def test_unresolvable_decorator_name_raises(self):
        def func():
            urlpatterns = [
                url(r'^$', views.sample_view, decorators=["does.not.exist"]),
            ]
        self.assertRaises(ImproperlyConfigured, func)

    def test_unresolvable_middleware_name_raises(self):
        def func():
            urlpatterns = [
                url(r'^$', views.sample_view, middleware_classes=["does.not.exist"]),
            ]
        self.assertRaises(ImproperlyConfigured, func)

    def test_decorators_can_be_used_in_iterable_urlpatterns(self):
        r = self.client.get("/attr/inc/decorators/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_can_be_used_in_iterable_urlpatterns(self):
        r = self.client.get("/attr/inc/middleware/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_decorators_can_be_applied_to_iterable_url(self):
        r = self.client.get("/attr/decorators/")
        self.assertEqual((r.args, r.kwargs),  (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_can_be_applied_to_iterable_url(self):
        r = self.client.get("/attr/middleware/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))


class ViewTypesTestCase(TestCase):

    def test_decorators_work_with_func_view(self):
        r = self.client.get("/decorators/inc/func/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_works_with_func_view(self):
        r = self.client.get("/middleware/inc/func/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_decorators_work_with_class_view(self):
        r = self.client.get("/decorators/inc/class/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_works_with_class_view(self):
        r = self.client.get("/middleware/inc/class/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_decorators_work_with_method_view(self):
        r = self.client.get("/decorators/inc/method/")
        self.assertEqual((r.args, r.kwargs), (
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_works_with_method_view(self):
        r = self.client.get("/middleware/inc/method/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))

    def test_decorators_work_with_generic_view(self):
        r = self.client.get("/decorators/inc/generic/")
        self.assertEqual((r.args, r.kwargs),(
            ("decorator 1 applied", "decorator 2 applied"), {}
        ))

    def test_middleware_works_with_generic_view(self):
        r = self.client.get("/middleware/inc/generic/")
        self.assertEqual((r.args, r.kwargs), (
            ("middleware 1 applied", "middleware 2 applied"), {}
        ))
