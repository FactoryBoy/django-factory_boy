import datetime

from django.conf import settings
from django.contrib.auth import models
from django.db.models import get_model

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
    content_type = factory.SubFactory(contenttypes.ContentTypeF)
    codename = factory.Sequence(lambda n:"factory_%s" % n)

class GroupF(factory.Factory):
    FACTORY_FOR = models.Group

    @classmethod
    def _setup_next_sequence(cls):
        return cls._associated_class.objects.values_list(
            'id', flat=True).order_by('-id')[0] + 1

    name = factory.Sequence(lambda n: "group%s" % n)

class UserF(factory.Factory):
    FACTORY_FOR = models.User

    @classmethod
    def _setup_next_sequence(cls):
        return cls._associated_class.objects.values_list(
            'id', flat=True).order_by('-id')[0] + 1

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

def user_create(cls, **kwargs):
    # figure out the profile's related name and strip profile's kwargs
    profile_model, profile_kwargs = None, {}
    try:
        app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
    except (ValueError, AttributeError):
        pass
    else:
        try:
            profile_model = get_model(app_label, model_name)
        except (ImportError, ImproperlyConfigured):
            pass
    if profile_model:
        user_field = profile_model._meta.get_field_by_name('user')[0]
        related_name = user_field.related_query_name()
        profile_prefix = '%s__' % related_name
        for k in kwargs.keys():
            if k.startswith(profile_prefix):
                profile_key = k.replace(profile_prefix, '', 1)
                profile_kwargs[profile_key] = kwargs.pop(k)

    # create the user
    user = cls._default_manager.create(**kwargs)

    if profile_model and profile_kwargs:
        # update or create the profile model
        profile, created = profile_model._default_manager.get_or_create(
            user=user, defaults=profile_kwargs)
        if not created:
            for k,v in profile_kwargs.items():
                setattr(profile, k, v)
            profile.save()
        setattr(user, related_name, profile)
        setattr(user, '_profile_cache', profile)

    return user
UserF.set_creation_function(user_create)

class MessageF(factory.Factory):
    FACTORY_FOR = models.Message

    user = factory.SubFactory(UserF)
    message = factory.Sequence(lambda n: "message %s" % n)
