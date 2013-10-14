# -*- coding: utf-8 -*-

from django.test import TestCase

from feedback_form.sitemaps import FeedbackSitemap


class FeedbackSitemapTest(TestCase):

    def setUp(self):
        self.sitemap = FeedbackSitemap()

    def test_items(self):
        self.assertEquals(len(self.sitemap.items()), 1)

        self.assertEquals(self.sitemap.location(
            self.sitemap.items()[0]), '/feedback/')
