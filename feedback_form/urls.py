# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from contact_form.views import ContactFormView

from .forms import FeedbackForm

urlpatterns = patterns('',
    url(r'^$', ContactFormView.as_view(form_class=FeedbackForm), name='contact_form'),
    url(r'^sent/$', RedirectView.as_view(url=reverse_lazy('contact_form')), name='contact_form_sent'),
)
