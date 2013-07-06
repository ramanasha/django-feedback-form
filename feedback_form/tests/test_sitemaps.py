# -*- coding: utf-8 -*-

from django.test import TestCase

from ..sitemaps import FeedbackSitemap


class FeedbackSitemapTest(TestCase):

    def setUp(self):
        self.base_url = 'http://testserver'

    def test_default(self):
        sitemap = FeedbackSitemap()
        self.assertEquals(len(sitemap.items()), 1)

        items = sitemap.items()
        self.assertEquals(sitemap.location(items[0]), '/feedback/')
