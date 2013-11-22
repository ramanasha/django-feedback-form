# -*- coding: utf-8 -*-

from django.contrib import messages
from django.utils.translation import ugettext as _

from contact_form.forms import AkismetContactForm


class FeedbackForm(AkismetContactForm):

    def save(self, fail_silently=False):
        super(FeedbackForm, self).save(fail_silently)
        messages.success(self.request, _("Your email was sent successfully!"))
