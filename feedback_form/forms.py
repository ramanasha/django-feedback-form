# -*- coding: utf-8 -*-

from django import forms
from django.db import transaction
from django.contrib import messages
from django.utils.translation import ugettext as _

from contact_form.forms import AkismetContactForm

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary.
attrs_dict = { 'class': 'required' }


class FeedbackForm(AkismetContactForm):

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(
            attrs=dict(attrs_dict, placeholder=_("John Doe")))
        self.fields['email'].widget = forms.TextInput(
            attrs=dict(attrs_dict, maxlength=200, placeholder=_("john.doe@example.com")))
        self.fields['body'].widget = forms.Textarea(
            attrs=dict(attrs_dict, placeholder=_("O hai, world!")))

    def save(self, fail_silently=False):
        with transaction.commit_on_success():
            super(FeedbackForm, self).save(fail_silently)
            messages.success(self.request, _(
                "Your email was sent successfully!"))
