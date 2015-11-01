# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0006_auto_20151101_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newstudent',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='newstudent',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='volunteer',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='newstudent',
            name='username',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='username',
        ),
        migrations.AddField(
            model_name='newstudent',
            name='rideuser_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=2, serialize=False, to='rideapp.RideUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='rideuser_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='rideapp.RideUser'),
            preserve_default=False,
        ),
    ]
