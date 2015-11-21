# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0003_auto_20151106_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideuser',
            name='isVolunteer',
            field=models.BooleanField(default=True),
        ),
    ]
