# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0008_auto_20151121_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideuser',
            name='name',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
