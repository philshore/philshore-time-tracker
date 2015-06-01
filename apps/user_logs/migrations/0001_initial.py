# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.IntegerField()),
                ('dateIn', models.DateField(verbose_name=b'Date In', blank=True)),
                ('timeIn', models.TimeField(verbose_name=b'time in', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeOut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.IntegerField()),
                ('dateOut', models.DateField(verbose_name=b'Date Out', blank=True)),
                ('timeOut', models.TimeField(verbose_name=b'time out', blank=True)),
            ],
        ),
    ]
