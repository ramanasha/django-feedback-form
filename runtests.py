#!/usr/bin/env python

import sys
from os import path

import django
from django.conf import settings, global_settings
from django.core.management import execute_from_command_line


if not settings.configured:
    BASE_DIR = path.dirname(path.realpath(__file__))

    settings.configure(
        DEBUG = False,
        TEMPLATE_DEBUG = True,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        TEMPLATE_DIRS = (
            path.join(BASE_DIR, 'test_templates'),
        ),
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.messages',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',

            'contact_form',
            'feedback_form',
        ),
        MIDDLEWARE_CLASSES = (
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ),
        TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner' if django.VERSION < (1,6) else 'django.test.runner.DiscoverRunner',
        SITE_ID = 1,
        ROOT_URLCONF = 'feedback_form.tests.test_urls',
    )

def runtests():
    argv = sys.argv[:1] + ['test', 'feedback_form'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
