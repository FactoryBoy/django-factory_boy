import datetime

from django.contrib.auth import models
from django.contrib.contenttypes import models as contenttypes_models

import factory
import factory.django


__all__ = (
    'UserFactory',
    'PermissionFactory',
    'GroupFactory'
)

class PermissionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Permission

    name = factory.Sequence(lambda n: "permission%s" % n)
    content_type = factory.Iterator(contenttypes_models.ContentType.objects.all())
    codename = factory.Sequence(lambda n: "factory_%s" % n)


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Group

    name = factory.Sequence(lambda n: "group%s" % n)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

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
