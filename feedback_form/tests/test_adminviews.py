# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from feedback_form.models import Feedback


class FeedbackAdminTest(TestCase):
    fixtures = ['users']

    model_info = {
        'name': 'user',
        'email': 'user@example.com',
        'body': 'o hai, world!',
        }

    def setUp(self):
        self.user = User.objects.get(username='jane')
        self.changelist_url = reverse('admin:feedback_form_feedback_changelist')

        self.client.login(username='john', password='123')  # login as superuser

    def test_anonymous(self):
        Feedback.objects.create(**self.model_info)

        response = self.client.get(self.changelist_url)
        self.failUnless("""<td class="field-email_link">user@example.com</td>""" in response.content)

    def test_authenticated(self):
        Feedback.objects.create(user=self.user, **self.model_info)

        response = self.client.get(self.changelist_url)
        self.failUnless("""<td class="field-email_link"><a href="/admin/auth/user/%s/">user@example.com</a></td>""" % self.user.pk in response.content)
