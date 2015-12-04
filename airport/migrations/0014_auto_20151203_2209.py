# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0013_auto_20151203_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideuser',
            name='address_at_duke',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rideuser',
            name='company',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rideuser',
            name='department_at_duke',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rideuser',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')]),
        ),
        migrations.AddField(
            model_name='rideuser',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rideuser',
            name='undergraduate_school',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rideuser',
            name='wechat',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
