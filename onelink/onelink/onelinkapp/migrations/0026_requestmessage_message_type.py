# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-11 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onelinkapp', '0025_auto_20170710_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestmessage',
            name='message_type',
            field=models.CharField(default='TEXT', max_length=10),
            preserve_default=False,
        ),
    ]
