# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

try:
    from django.contrib.auth import get_user_model

    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

from ..models import Feedback


class FeedbackAdminTest(TestCase):

    model_info = {
        'name': 'user',
        'email': 'user@example.com',
        'body': 'o hai, world!',
    }

    def setUp(self):
        User.objects.create_superuser(username='admin', email='admin@example.com', password='123')

        self.user = User.objects.create_user(username='user', email='user@example.com')
        self.changelist_url = reverse('admin:feedback_form_feedback_changelist')
        self.client.login(username='admin', password='123')  # login as superuser

    def test_anonymous(self):
        Feedback.objects.create(**self.model_info)

        response = self.client.get(self.changelist_url)
        self.assertTrue("""user@example.com""" in str(response.content))

    def test_authenticated(self):
        Feedback.objects.create(user=self.user, **self.model_info)

        response = self.client.get(self.changelist_url)
        self.assertTrue(
            """<a href="/admin/auth/user/%s/">user@example.com</a>""" % (self.user.pk) in str(response.content))
            
