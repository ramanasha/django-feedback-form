# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.contrib import messages
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _

from contact_form.forms import ContactForm

from .models import Feedback

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary.
attrs_dict = { 'class': 'required' }


class AkismetContactForm(ContactForm):
    """
    Contact form which doesn't add any extra fields, but does add an
    Akismet spam check to the validation routine.

    Requires the setting ``AKISMET_API_KEY``, which should be a valid
    Akismet API key.

    """
    def clean_body(self):
        """
        Perform Akismet validation of the message.

        """
        if 'body' in self.cleaned_data and getattr(settings, 'AKISMET_API_KEY', ''):
            from akismet import Akismet
            akismet_api = Akismet(
                key=settings.AKISMET_API_KEY,
                blog_url='http://%s/' % Site.objects.get_current().domain,
            )
            if akismet_api.verify_key():
                akismet_data = {
                    'comment_type': 'comment',
                    'referer': self.request.META.get('HTTP_REFERER', ''),
                    'user_ip': self.request.META.get('REMOTE_ADDR', ''),
                    'user_agent': self.request.META.get('HTTP_USER_AGENT', ''),
                }
                if akismet_api.comment_check(
                        smart_str(self.cleaned_data['body']), data=akismet_data, build_data=True):
                    raise forms.ValidationError(_("Akismet thinks this message is spam"))
        return self.cleaned_data['body']


class FeedbackForm(AkismetContactForm):

    def __init__(self, *args, **kwargs):
        request = kwargs.get('request', None)

        initial = {}
        if hasattr(request, 'user') and request.user.is_authenticated():
            initial.update({
                'name': request.user.get_full_name(),
                'email': request.user.email,
            })
        kwargs['initial'].update(initial)

        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(
            attrs=dict(attrs_dict, placeholder=_("John Doe")))
        self.fields['email'].widget = forms.TextInput(
            attrs=dict(attrs_dict, maxlength=200, placeholder=_("john.doe@example.com")))
        self.fields['body'].widget = forms.Textarea(
            attrs=dict(attrs_dict, placeholder=_("O hai, world!")))

    def save(self, fail_silently=False):
        fb = Feedback(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            body=self.cleaned_data['body'],
        )
        if self.request.user.is_authenticated():
            fb.user = self.request.user
        fb.save()

        super(FeedbackForm, self).save(fail_silently)
        messages.success(
            self.request, _("Your email was sent successfully!"))
