# -*- coding: utf-8 -*-

from django import forms
from django.contrib import messages
from django.utils.translation import ugettext as _

from contact_form.forms import ContactForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div, ButtonHolder

__all__ = ['FeedbackForm']


class FeedbackForm(ContactForm):

    honeypot = forms.CharField(required=False, label=_("""If you enter anything in this field your comment will be treated as spam"""))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('name', css_class='input-xlarge'),
        Field('email', css_class='input-xlarge'),
        Field('body', rows="6", css_class='input-xxlarge'),
        'honeypot',
        ButtonHolder(
            Div(Submit('submit', _("Send message"), css_class="btn-success"), css_class='controls'),
            css_class='control-group',
        )
    )

    def clean_honeypot(self):
        """Check that nothing's been entered into the honeypot."""
        value = self.cleaned_data["honeypot"]
        if value:
            raise forms.ValidationError(self.fields["honeypot"].label)
        return value

    def save(self, fail_silently=False):
        super(FeedbackForm, self).save(fail_silently)
        messages.success(self.request, _("Your email was sent successfully!"))
