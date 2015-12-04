# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0012_newstudent_arrival_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rideuser',
            name='address_at_duke',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='citizenship',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='company',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='department_at_duke',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='undergraduate_school',
        ),
        migrations.RemoveField(
            model_name='rideuser',
            name='wechat',
        ),
    ]
