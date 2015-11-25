# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0006_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='car_plate',
            field=models.ForeignKey(to='airportapp.Car'),
        ),
    ]
