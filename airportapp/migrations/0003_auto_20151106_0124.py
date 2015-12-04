# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0002_auto_20151101_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='available_time',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='car_plate',
        ),
    ]
