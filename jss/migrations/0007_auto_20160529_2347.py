# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jss', '0006_auto_20160529_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jss.Site'),
        ),
    ]
