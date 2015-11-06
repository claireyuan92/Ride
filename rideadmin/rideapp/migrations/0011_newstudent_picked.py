# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0010_remove_volunteer_available_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='picked',
            field=models.BooleanField(default=False),
        ),
    ]
