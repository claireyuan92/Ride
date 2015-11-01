# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('plate_number', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('plate_number', models.CharField(max_length=256, serialize=False, primary_key=True)),
                ('arrival_time', models.DateTimeField()),
                ('terminal', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NewStudent',
            fields=[
                ('rideuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rideapp.RideUser')),
                ('luggage_checked_num', models.IntegerField()),
                ('luggage_carryon_num', models.IntegerField()),
                ('backpack_num', models.IntegerField()),
                ('flight', models.ForeignKey(to='rideapp.Flight')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('rideapp.rideuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('newstudent', models.ForeignKey(to='rideapp.NewStudent')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('rideuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rideapp.RideUser')),
                ('available_time', models.DurationField()),
                ('driver_license', models.CharField(max_length=50)),
                ('car_plate', models.ForeignKey(to='rideapp.Car')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('rideapp.rideuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='rideuser',
            name='address_at_duke',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rideuser',
            name='age',
            field=models.IntegerField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rideuser',
            name='company',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rideuser',
            name='department_at_duke',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rideuser',
            name='phone',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rideuser',
            name='undergraduate_school',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rideuser',
            name='wechat',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='pickup',
            name='volunteer',
            field=models.ForeignKey(to='rideapp.Volunteer'),
        ),
    ]
