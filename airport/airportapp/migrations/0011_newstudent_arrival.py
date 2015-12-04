# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airportapp', '0010_newstudent_haspickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='arrival',
            field=models.TimeField(null=True),
        ),
    ]
