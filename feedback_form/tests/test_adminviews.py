# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from contact_form.models import Feedback


class FeedbackAdminTest(TestCase):
    fixtures = ['users']

    model_info = {
        'name': 'user',
        'email': 'user@example.com',
        'body': 'o hai, world!',
        }

    def setUp(self):
        self.user = User.objects.get(username='jane')
        self.client.login(username='john', password='123')
        self.changelist_url = reverse('admin:contact_form_feedback_changelist')

    def test_anonymous(self):
        Feedback.objects.create(**self.model_info)

        response = self.client.get(self.changelist_url)

        self.failUnless("<td>user@example.com</td>" in response.content)

    def test_authenticated(self):
        Feedback.objects.create(user=self.user, **self.model_info)

        response = self.client.get(self.changelist_url)

        self.failUnless("""td><a href="/admin/auth/user/%s/">user@example.com</a></td>""" % self.user.pk in response.content)
