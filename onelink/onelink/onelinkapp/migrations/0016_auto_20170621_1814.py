# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onelinkapp', '0015_auto_20170620_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemorderhistory',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemorderhistory',
            name='payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='itemorderhistory',
            name='payment_state',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='itemorderhistory',
            name='payment_time',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='payment_state',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='itemrequest',
            name='payment_time',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]