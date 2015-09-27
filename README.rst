django-feedback-form
====================

django-feedback-form application provides simple, extensible
feedback-form functionality for `Django <https://djangoproject.com/>`_
sites.

.. image:: https://img.shields.io/pypi/v/django-feedback-form2.svg
    :target: https://pypi.python.org/pypi/django-feedback-form2/

.. image:: https://img.shields.io/pypi/dm/django-feedback-form2.svg
    :target: https://pypi.python.org/pypi/django-feedback-form2/

.. image:: https://img.shields.io/github/license/bashu/django-feedback-form.svg
    :target: https://pypi.python.org/pypi/django-feedback-form2/

.. image:: https://img.shields.io/travis/bashu/django-feedback-form.svg
    :target: https://travis-ci.org/bashu/django-feedback-form/

.. image:: https://landscape.io/github/bashu/django-feedback-form/develop/landscape.svg?style=flat
    :target: https://landscape.io/github/bashu/django-feedback-form/develop

Installation
------------

Either checkout ``feedback_form`` from GitHub, or install using ``pip`` :

.. code-block:: bash

    pip install django-feedback-form

Setup
-----

Add ``feedback_form`` (and ``contact_form``) to  ``INSTALLED_APPS`` :

.. code-block:: python
                
    import django

    INSTALLED_APPS += (
        'contact_form',
        'feedback_form',
    )

    if django.VERSION < (1, 7):
        INSTALLED_APPS += (
            'south',
        )

Update your ``urls.py`` file :

.. code-block:: python

    urlpatterns += patterns('',
        url(r'^feedback/', include('feedback_form.urls')),
    )       

Then run ``python ./manage.py syncdb`` to create the required database
tables. And that should be it!

Please see ``example`` application. This application is used to manually
test the functionalities of this package. This also serves as a good
example.

You need Django 1.4 or above to run that. It might run on older
versions but that is not tested.

License
-------

``django-feedback-form`` is released under the BSD license.
