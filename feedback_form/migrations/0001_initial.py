# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=75, verbose_name='e-mail')),
                ('body', models.TextField(verbose_name='message')),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
            bases=(models.Model,),
        ),
    ]
