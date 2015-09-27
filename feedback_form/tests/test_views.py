# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class FeedbackViewTest(TestCase):

    post_data = {
        'name': 'Joe User',
        'email': 'joeuser@example.com',
        'body': 'Hello, World!',
    }

    def test_post_with_redirect(self):
        response = self.client.post(reverse('contact_form'), self.post_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(reverse('contact_form_sent') in response['Location'])

        response = self.client.get(response['Location'])

        self.assertEqual(response.status_code, 301)
        self.assertTrue(reverse('contact_form') in response['Location'])

        response = self.client.get(response['Location'])

        # check for success message...
        for m in response.context['messages']:
            self.assertTrue("Your email was sent successfully!", unicode(m))
