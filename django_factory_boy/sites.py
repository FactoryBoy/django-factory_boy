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
