import unittest2
import doctest

from django.conf import settings
from django.core.management import call_command

settings.configure(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}, INSTALLED_APPS=['django.contrib.auth', 'django.contrib.contenttypes']
)

def get_suite():
    call_command('syncdb', interactive=False)
    loader = unittest2.TestLoader()
    suite = loader.discover('django_factory_boy')

    return suite

if __name__ == '__main__':
    result = unittest2.TestResult()
    get_suite().run(result)
    for error in result.errors:
        print error
