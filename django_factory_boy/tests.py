from factory import Factory
import unittest

from . import auth
from . import sites

class TestSimple(unittest.TestCase):
    def _test_app(self, module):
        """Test a single app."""
        for f_prop in dir(module):
            F = getattr(module, f_prop)
            if isinstance(F, type) and issubclass(F, Factory):
                F()

    def test_auth(self):
        self._test_app(auth)

    def test_sites(self):
        self._test_app(sites)
