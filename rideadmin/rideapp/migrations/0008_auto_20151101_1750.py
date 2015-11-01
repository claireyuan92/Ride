# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0007_auto_20151101_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newstudent',
            options={'verbose_name': 'NewStudent'},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'verbose_name': 'Volunteer'},
        ),
    ]
