#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2011-2013 Raphaël Barrois
# This code is distributed under the two-clause BSD License.

import codecs
import os
import re
import sys

from setuptools import setup

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    init_path = os.path.join(root_dir, *(package_components + ['__init__.py']))
    with codecs.open(init_path, 'r', 'utf-8') as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


PACKAGE = 'django_factory_boy'


setup(
    name='django-factory_boy',
    version=get_version(PACKAGE),
    description="Uses factory_boy to supply test data factory classes for all stock Django models.",
    author='Votizen',
    author_email='team@votizen.com',
    maintainer='Raphaël Barrois',
    maintainer_email='raphael.barrois+fboy@polytechnique.org',
    url='http://github.com/rbarrois/django-factory_boy',
    keywords=['factory_boy', 'django', 'fixtures'],
    packages=[PACKAGE],
    license="BSD",
    install_requires=[
        'Django>=1.6',
        'factory_boy>=2.6.0',
    ],
    setup_requires=[
        'setuptools>=0.8',
    ],
    tests_require=[
        'Django>=1.3',
        'factory_boy>=1.0.4'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite='runtests.runtests',
)
