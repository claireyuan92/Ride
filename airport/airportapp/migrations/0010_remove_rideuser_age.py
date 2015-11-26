# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0009_rideuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rideuser',
            name='age',
        ),
    ]
