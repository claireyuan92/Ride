# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0011_newstudent_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='arrival_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
