# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class FeedbackAdminTest(TestCase):

    def setUp(self):
        # create superuser account...
        User.objects.create_superuser(username='admin', email='admin@example.com', password='123')

    def tearDown(self):
        User.objects.filter(username='admin').delete()

    def test_default(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('admin:contact_form_feedback_changelist'))
