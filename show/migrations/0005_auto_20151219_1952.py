# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_auto_20151126_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='mode',
            fields=[
                ('recordId', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('sportMode', models.IntegerField()),
                ('heartRate', models.IntegerField()),
                ('altOffset', models.FloatField()),
                ('planeOffset', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='data1',
        ),
        migrations.DeleteModel(
            name='rid_table',
        ),
    ]
