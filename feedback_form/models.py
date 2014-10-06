# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Feedback(models.Model):

    user = models.ForeignKey(User, null=True, verbose_name=_("user"))

    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('e-mail'))
    body = models.TextField(_("message"))

    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")
