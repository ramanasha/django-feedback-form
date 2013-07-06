# -*- coding: utf-8 -*-

from django.conf.urls.defaults import url, patterns
from django.views.generic.simple import redirect_to

from .forms import FeedbackForm

urlpatterns = patterns('',
    url(r'^$', 'contact_form.views.contact_form', {'form_class': FeedbackForm}, name='contact_form'),
    url(r'^sent/$', redirect_to, {'url': '../'}, name='contact_form_sent'),
)
