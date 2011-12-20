import datetime

from django.conf import settings

from django.contrib.auth import models

from django_factory_boy import contenttypes

import factory

__all__ = (
    'UserF',
    'PermissionF',
    'GroupF'
)

class PermissionF(factory.Factory):
    FACTORY_FOR = models.Permission

    name = factory.Sequence(lambda n: "permission%s" % n)
    content_type = contenttypes.ContentTypeF()
    codename = factory.Sequence(lambda n:"factory_%s" % n)

class GroupF(factory.Factory):
    FACTORY_FOR = models.Group

    name = factory.Sequence(lambda n: "group%s" % n)

class UserF(factory.Factory):
    FACTORY_FOR = models.User

    username = factory.Sequence(lambda n: "username%s" % n)
    first_name = factory.Sequence(lambda n: "first_name%s" % n)
    last_name = factory.Sequence(lambda n: "last_name%s" % n)
    email = factory.Sequence(lambda n: "email%s@example.com" % n)
    password = 'sha1$caffc$30d78063d8f2a5725f60bae2aca64e48804272c3'
    is_staff = False
    is_active = True
    is_superuser = False
    last_login = datetime.datetime(2000, 1, 1)
    date_joined = datetime.datetime(1999, 1, 1)

class MessageF(factory.Factory):
    FACTORY_FOR = models.Message

    user = UserF()
    message = factory.Sequence(lambda n: "message %s" % n)
