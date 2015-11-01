# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0008_auto_20151101_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='plate_number',
            new_name='flight_number',
        ),
    ]
