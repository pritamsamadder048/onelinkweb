# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onelinkapp', '0005_auto_20170619_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_type',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
