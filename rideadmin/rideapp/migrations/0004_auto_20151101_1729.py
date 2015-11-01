# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0003_auto_20151101_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rideuser',
            options={'verbose_name': 'RideUser'},
        ),
    ]
