django_factory_boy
==================

When testing a ``django`` app, a common case is to create some data,
then test app behavior around that test data.
This is usually `done with fixtures`_, but `this includes some pain`_.

`factory_boy`_ is useful for concisely creating objects, particularly for test data.

This project will supply factory_boy classes for each model Django ships.
The factories are named after the class it constructs.
For example, a factory for ``django.contrib.auth.models.User`` is available at ``django_factory_boy.auth.UserFactory``.

See ``factory_boy`` for detailed docs, but all fields are given default values which can be overriden by passing keyword arguments to the constructor.  For example::

    from django_factory_boy import auth as auth_factories
    user = auth_factories.UserFactory(first_name="test")

would result in a saved ``User`` instance whose ``first_name`` is set to ``"test"``.

The resulting objects are normal ``django`` model instances, so once they are constructed you can use them in the normal ways.

Not all ``django`` models have been added yet; if you need one, open an issue or a pull request.  Currently supported:

- contrib.auth (``UserFactory``, ``GroupFactory``, ``PermissionFactory``)
- contrib.sites (``SiteFactory``)


This project intends to support all Python versions which Django does - 2.6 - 3.4 as of Django 1.6.
It supports all Django versions from 1.6 onwards.

.. _`factory_boy`: https://github.com/rbarrois/factory_boy
.. _`done with fixtures`: https://docs.djangoproject.com/en/1.3/topics/testing/#fixture-loading
.. _`this includes some pain`: http://groups.google.com/group/django-developers/browse_thread/thread/d9a9ca573dfb6f87
