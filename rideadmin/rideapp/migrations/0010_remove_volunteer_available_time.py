# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0009_auto_20151101_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='available_time',
        ),
    ]
