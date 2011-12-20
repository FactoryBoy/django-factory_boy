When testing Django app, a common case is to create some data, then test app behavior around that test data.  This is usually [done with fixtures][fixtures], but [this includes some pain][fixturepain].

[rbarrois/factory_boy][factory_boy] is useful for briefly creating objects, particularly for test data.

This project will supply factory_boy classes for each model Django ships.  The factories are named after the class it constructs.  For example, a factory for django.contrib.auth.models.User is available at django_factoryboy.auth.UserF.

See [factory_boy][factoryboy] for detailed docs, but all fields are given default values which can be overriden by passing keyword arguments to the constructor.  For example:

    from django_factoryboy.auth import UserF
    user = UserF(first_name="test")

would result in a saved User instance whose first_name is set to "test".

The resulting objects are normal Django model instances, so once they are constructed you can use them in the normal ways.

Not all Django models have been added yet; if you need one, open an issue or a pull request.  Currently supported:

    contrib.contenttypes
    contrib.auth


This project intends to support all Python versions which Django does - 2.4 - 2.7 as of Django 1.3.
  (I have not verified that factoryboy itself supports back to 2.4)

-  @jdunck

[factory_boy]: https://github.com/rbarrois/factory_boy
[fixtures]: https://docs.djangoproject.com/en/1.3/topics/testing/#fixture-loading
[fixturepain]: http://groups.google.com/group/django-developers/browse_thread/thread/d9a9ca573dfb6f87
