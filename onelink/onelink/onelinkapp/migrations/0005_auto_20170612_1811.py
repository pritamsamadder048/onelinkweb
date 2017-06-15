# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onelinkapp', '0004_auto_20170609_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('itemmap_id', models.IntegerField()),
                ('itemmap_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onelinkapp.ItemMap')),
            ],
        ),
        migrations.CreateModel(
            name='ItemNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceprovider_id', models.IntegerField()),
                ('itemrequest_id', models.IntegerField()),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('notification', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceprovider_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('item_map_id', models.IntegerField()),
                ('item_request_id', models.IntegerField()),
                ('booked_time', models.DateTimeField(auto_now_add=True)),
                ('item_map_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iohservicemap', to='onelinkapp.ItemMap')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceprovider_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('item_category_id', models.IntegerField()),
                ('item_map_id', models.IntegerField()),
                ('item_quantity', models.IntegerField(default=1)),
                ('areapincode', models.PositiveIntegerField(blank=True, null=True)),
                ('item_request_address', models.TextField(blank=True, null=True)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('request_detail', models.TextField(blank=True, null=True)),
                ('item_status', models.IntegerField(default=0)),
                ('item_map_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onelinkapp.ItemMap')),
                ('serviceprovider_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemproviderdetail', to='onelinkapp.UserDetail')),
                ('user_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemuserdetail', to='onelinkapp.UserDetail')),
            ],
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='service_time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='itemorderhistory',
            name='item_request_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iohsitemrequest', to='onelinkapp.ItemRequest'),
        ),
        migrations.AddField(
            model_name='itemorderhistory',
            name='serviceprovider_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iohproviderdetail', to='onelinkapp.UserDetail'),
        ),
        migrations.AddField(
            model_name='itemorderhistory',
            name='user_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iohuserdetail', to='onelinkapp.UserDetail'),
        ),
        migrations.AddField(
            model_name='itemnotification',
            name='itemrequest_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onelinkapp.ItemRequest'),
        ),
        migrations.AddField(
            model_name='itemnotification',
            name='serviceprovider_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inotiproviderdetail', to='onelinkapp.UserDetail'),
        ),
    ]
