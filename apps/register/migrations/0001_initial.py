# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_auto_20160108_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComponent',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('component', models.CharField(max_length=100)),
            ],
        ),
    ]
