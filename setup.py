#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-factory_boy',
    version='0.1.6', # remember to change django_factory_boy/__init__.py
    author='Votizen',
    author_email='team@votizen.com',
    url='http://github.com/votizen/django-factory_boy',
    description = 'Uses factory_boy to supply test data factory classes for all stock Django models.',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['factory_boy>=1.0.4'],
    include_package_data=True,
    tests_require=[
        'unittest2>=0.5.1',
        'django>=1.3',
        'factory_boy>=1.0.4'
    ],
    test_suite='runtests.get_suite',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

