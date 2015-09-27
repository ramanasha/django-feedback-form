# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatewords
from django.utils.encoding import python_2_unicode_compatible

try:
    User = settings.AUTH_USER_MODEL
except AttributeError:
    from django.contrib.auth.models import User


@python_2_unicode_compatible
class Feedback(models.Model):

    user = models.ForeignKey(User, null=True, verbose_name=_("user"))

    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('e-mail'))
    body = models.TextField(_("message"))

    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")

    def __str__(self):
        return truncatewords(self.body, 16)
