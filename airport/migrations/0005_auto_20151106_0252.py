# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0004_rideuser_isvolunteer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='terminal',
        ),
        migrations.RemoveField(
            model_name='newstudent',
            name='backpack_num',
        ),
        migrations.RemoveField(
            model_name='newstudent',
            name='luggage_carryon_num',
        ),
        migrations.RemoveField(
            model_name='newstudent',
            name='luggage_checked_num',
        ),
    ]
