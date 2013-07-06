# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.admin.sites import NotRegistered
from django.utils.translation import ugettext_lazy as _

from contact_form.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    date_hierarchy = "sent_time"
    list_display = ('name', 'email_link', 'sent_time')
    fields = ('user', 'name', 'email', 'body')
    search_fields = ('name', 'email', 'body')
    raw_id_fields = ('user',)

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedback")

    @classmethod
    def email_link(cls, obj):
        if obj.user_id is not None:
            return """<a href="%(url)s">%(email)s</a>""" % {
                'url': reverse('admin:auth_user_change', args=[obj.user_id]),
                'email': obj.email,
                }
        return obj.email
    email_link.short_description = _("email")
    email_link.admin_order_field = 'email'
    email_link.allow_tags = True

try:
    admin.site.unregister(Feedback)
except NotRegistered:
    pass
admin.site.register(Feedback, FeedbackAdmin)
