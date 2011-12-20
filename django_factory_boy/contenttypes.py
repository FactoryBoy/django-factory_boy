from django.conf import settings
from django.contrib.contenttypes import models
from django.db.models import Model

import factory

__all__ = (
    'ContentTypeF',
)

def get_model(app_label):
    try:
        app_models = __import__("%s.%s" % (app_label, 'models'), {}, {}, ['*'])
    except ImportError:
        return None

    for prop in dir(app_models):
        attr = getattr(app_models, prop)
        try:
            if issubclass(attr, Model):
                return attr
        except TypeError:
            pass # not a class at all.
    else:
        return None

class ContentTypeF(factory.Factory):
    FACTORY_FOR = models.ContentType

    name = factory.Sequence(lambda n: "content type %s" % n)
    @factory.lazy_attribute
    def app_label(a):
        for label_maybe in settings.INSTALLED_APPS:
            model = get_model(label_maybe)
            if not model is None:
                # avoid returning a model which is imported into this app, but 
                #  not actually part of this app 
                if label_maybe.endswith(model._meta.app_label):
                    return label_maybe
        else:
            raise ValueError("No INSTALLED_APP has a model; please do that before trying to construct a ContentTypeF.")

    @factory.lazy_attribute
    def model(a):
        return get_model(a.app_label)
    
def CTF_create(cls, **kwargs):
    app_label = kwargs.pop('app_label')
    model = kwargs.pop('model')
    return models.ContentType.objects.get_or_create(
        app_label=app_label,
        model=model._meta.module_name, defaults=kwargs)[0]

ContentTypeF.set_creation_function(CTF_create)
