# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import RequestFactory

from ..forms import FeedbackForm


class FeedbackFormTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_akismet(self):
        request = self.factory.get('feedback/')

        data = {
            'name': 'spammer',
            'email': 'spam@camp.com',
            'body': 'viagra, cialis, porn',
            }
        form = FeedbackForm(request=request, data=data)
        self.failIf(form.is_valid())
