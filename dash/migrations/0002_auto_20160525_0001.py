# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 00:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreferences',
            name='id',
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='userpreferences', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
