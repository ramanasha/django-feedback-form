# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from contact_form.models import Feedback


class FeedbackAdminTest(TestCase):

    model_info = {
        'name': 'user',
        'email': 'user@example.com',
        'body': 'o hai, world!',
        }

    def setUp(self):
        # create superuser account...
        User.objects.create_superuser(username='admin', email='admin@example.com', password='123')
        Feedback.objects.create(**self.model_info)

    def tearDown(self):
        User.objects.filter(username='admin').delete()

    def test_default(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('admin:contact_form_feedback_changelist'))

        self.failUnless("<td>user@example.com</td>" in response.content)


    def test_email_link(self):
        user = User.objects.create_user(username='user', email='user@example.com')
        Feedback.objects.create(user=user, **self.model_info)

        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('admin:contact_form_feedback_changelist'))
        self.failUnless("""td><a href="/admin/auth/user/%s/">user@example.com</a></td>""" % user.pk in response.content)
