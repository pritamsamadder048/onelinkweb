# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onelinkapp', '0006_review_review_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_type',
            field=models.CharField(max_length=40),
        ),
    ]
