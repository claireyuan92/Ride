# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0010_remove_rideuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rideuser',
            name='wechat',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
