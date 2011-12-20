from factory import Factory
import unittest2 as unittest

class TestSimple(unittest.TestCase):
    def _test_app(self, module):
        for f_prop in dir(module):
            F = getattr(module, f_prop)
            try:
                is_sub = issubclass(F, Factory)
            except TypeError: # not a subclass at all.
                is_sub = False
            else:
                if is_sub:
                    F()

    def test_auth(self):
        from django_factory_boy import auth
        self._test_app(auth)

    def test_contenttypes(self):
        from django_factory_boy import contenttypes
        self._test_app(contenttypes)
