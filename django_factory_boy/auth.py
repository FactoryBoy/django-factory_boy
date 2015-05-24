# -*- coding: utf-8 -*-
# Copyright (c) 2011-2012 Votizen
# Copyright (c) 2013-2015 Raphaël Barrois
# This code is distributed under the two-clause BSD License.

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

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

    is_active = True
    is_staff = False
    is_superuser = False

    last_login = datetime.datetime(2000, 1, 1)
    date_joined = datetime.datetime(1999, 1, 1)
