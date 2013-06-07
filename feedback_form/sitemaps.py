# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

__all__ = ['FeedbackSitemap']


class FeedbackSitemap(Sitemap):
    changefreq = "never"
    lastmod = None

    def items(self):
        return ['contact_form']

    def location(self, obj):
        return reverse(obj)
