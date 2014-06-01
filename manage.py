# -*- coding: utf-8 -*-

import os, sys

#from django.core.management import execute_from_command_line
from django.core.management import ManagementUtility

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

    'contact_form',
    'django_jenkins',
    ] + PROJECT_APPS

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'test_templates'),
    ]

SITE_ID = 1

ROOT_URLCONF = 'test_urls'

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
        SITE_ID = SITE_ID,
        PROJECT_APPS = PROJECT_APPS,
        JENKINS_TASKS = JENKINS_TASKS,
        COVERAGE_EXCLUDES_FOLDERS = COVERAGE_EXCLUDES_FOLDERS,
        PYLINT_RCFILE = PYLINT_RCFILE,
        TEMPLATE_DIRS = TEMPLATE_DIRS,
        TEMPLATE_DEBUG = TEMPLATE_DEBUG
        )
    utility = ManagementUtility(sys.argv)
    utility.execute()
