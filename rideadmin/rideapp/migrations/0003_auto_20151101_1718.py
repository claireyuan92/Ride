# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0002_auto_20151101_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rideuser',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
