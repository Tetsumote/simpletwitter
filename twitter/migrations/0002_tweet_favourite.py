# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-31 10:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='user_favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
