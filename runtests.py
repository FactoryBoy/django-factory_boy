#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2011-2013 Raphaël Barrois
# This code is distributed under the two-clause BSD license.

from __future__ import unicode_literals

import sys

# Generic Django imports
import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django_factory_boy',
        ],
    )

# "configuration required" django imports
if django.VERSION >= (1, 7, 0):
    django.setup()

if django.VERSION <= (1, 8, 0):
    from django.test.simple import DjangoTestSuiteRunner
else:
    from django.test.runner import DiscoverRunner as DjangoTestSuiteRunner


def runtests(*test_args):
    if not test_args:
        test_args = ('django_factory_boy',)
    runner = DjangoTestSuiteRunner(failfast=False)
    failures = runner.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
