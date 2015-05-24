# -*- coding: utf-8 -*-
# Copyright (c) 2011-2012 Votizen
# Copyright (c) 2013-2015 Raphaël Barrois
# This code is distributed under the two-clause BSD License.

from django.contrib.sites.models import Site

import factory
import factory.django

__all__ = (
    'SiteFactory',
)


class SiteF(factory.django.DjangoModelFactory):
    class Meta:
        model = Site

    name = factory.Sequence(lambda n: "site%s" % n)
    domain = factory.Faker('domain_name')
