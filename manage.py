# -*- coding: utf-8 -*-

import os

from django.core.management import execute_manager

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
        }
    }

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    ]

PROJECT_APPS = [
    'feedback_form',
    ]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',

    'crispy_forms',
    'contact_form',
    'django_jenkins',
    'discover_runner',
    ] + PROJECT_APPS

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'test_templates'),
    ]

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap'

ROOT_URLCONF = 'test_urls'

TEST_RUNNER = 'discover_runner.DiscoverRunner'

JENKINS_TASKS = (
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    )

COVERAGE_EXCLUDES_FOLDERS = ['feedback_form/tests/*']
PYLINT_RCFILE = os.path.join(PROJECT_ROOT, 'pylint.rc')

if __name__ == "__main__":
    from django.conf import settings
    settings.configure(
        DATABASES = DATABASES,
        INSTALLED_APPS = INSTALLED_APPS,
        ROOT_URLCONF = ROOT_URLCONF,
        MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES,
        CRISPY_TEMPLATE_PACK = CRISPY_TEMPLATE_PACK,
        SITE_ID = SITE_ID,
        PROJECT_APPS = PROJECT_APPS,
        TEST_RUNNER = TEST_RUNNER,
        JENKINS_TASKS = JENKINS_TASKS,
        COVERAGE_EXCLUDES_FOLDERS = COVERAGE_EXCLUDES_FOLDERS,
        PYLINT_RCFILE = PYLINT_RCFILE,
        TEMPLATE_DIRS = TEMPLATE_DIRS,
        TEMPLATE_DEBUG = TEMPLATE_DEBUG
        )
    execute_manager(settings)
