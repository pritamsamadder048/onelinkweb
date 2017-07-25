# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import onelinkapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('onelinkapp', '0027_auto_20170720_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmap',
            name='height_field1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='height_field2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='height_field3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='height_field4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='height_field5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='item_image1',
            field=models.ImageField(blank=True, height_field='height_field1', null=True, upload_to=onelinkapp.models.item_image_upload_location, width_field='width_field1'),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='item_image2',
            field=models.ImageField(blank=True, height_field='height_field2', null=True, upload_to=onelinkapp.models.item_image_upload_location, width_field='width_field2'),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='item_image3',
            field=models.ImageField(blank=True, height_field='height_field3', null=True, upload_to=onelinkapp.models.item_image_upload_location, width_field='width_field3'),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='item_image4',
            field=models.ImageField(blank=True, height_field='height_field4', null=True, upload_to=onelinkapp.models.item_image_upload_location, width_field='width_field4'),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='item_image5',
            field=models.ImageField(blank=True, height_field='height_field5', null=True, upload_to=onelinkapp.models.item_image_upload_location, width_field='width_field5'),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='width_field1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='width_field2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='width_field3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='width_field4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmap',
            name='width_field5',
            field=models.IntegerField(default=0),
        ),
    ]