# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rideapp', '0004_auto_20151101_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newstudent',
            options={},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={},
        ),
        migrations.AlterModelManagers(
            name='newstudent',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='volunteer',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='newstudent',
            name='rideuser_ptr',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='rideuser_ptr',
        ),
        migrations.AddField(
            model_name='newstudent',
            name='username',
            field=models.OneToOneField(primary_key=True, default=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='username',
            field=models.OneToOneField(primary_key=True, default=1, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='plate_number',
            field=models.CharField(default=True, max_length=20, serialize=False, primary_key=True),
        ),
    ]
