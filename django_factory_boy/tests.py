# -*- coding: utf-8 -*-
# Copyright (c) 2011-2012 Votizen
# Copyright (c) 2013-2015 Raphaël Barrois
# This code is distributed under the two-clause BSD License.

import unittest
import factory

from . import auth
from . import sites

class TestSimple(unittest.TestCase):
    def _test_app(self, module):
        """Test a single app."""
        for f_prop in dir(module):
            F = getattr(module, f_prop)
            if isinstance(F, type) and issubclass(F, factory.Factory):
                F()

    def test_auth(self):
        self._test_app(auth)

    def test_sites(self):
        self._test_app(sites)
