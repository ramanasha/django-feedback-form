# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class ViewTest(TestCase):

    def setUp(self):
        self.base_url = 'http://testserver'

    def test_success_case_with_redirect(self):
        data = {
            'name': 'Joe User',
            'email': 'joeuser@example.com',
            'body': 'Hello, World!',
            }
        response = self.client.post(reverse('contact_form'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '%s%s' % (self.base_url, reverse('contact_form_sent')))

        response = self.client.get(response['Location'])
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], '%s%s' % (self.base_url, reverse('contact_form')))

        response = self.client.get(response['Location'])

        # check for success message...
        for m in response.context['messages']:
            self.assertTrue("Your email was sent successfully!", unicode(m))
