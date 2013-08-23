# -*- coding: utf-8 -*-

from django.test import TestCase

from feedback_form.sitemaps import FeedbackSitemap


class FeedbackSitemapTest(TestCase):

    def setUp(self):
        self.base_url = 'http://testserver'
        self.sitemap = FeedbackSitemap()

    def test_count(self):
        self.assertEquals(len(self.sitemap.items()), 1)

    def test_items(self):
        self.assertEquals(self.sitemap.location(
                self.sitemap.items()[0]), '/feedback/')
