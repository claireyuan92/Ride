# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0007_auto_20151106_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
    ]
