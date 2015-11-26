# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('altOffset', models.DecimalField(max_digits=26, decimal_places=16)),
                ('altitude', models.DecimalField(max_digits=26, decimal_places=16)),
                ('deviceX', models.DecimalField(max_digits=26, decimal_places=16)),
                ('deviceY', models.DecimalField(max_digits=26, decimal_places=16)),
                ('deviceZ', models.DecimalField(max_digits=26, decimal_places=16)),
                ('heartRate', models.IntegerField()),
                ('isIntegerKM', models.IntegerField()),
                ('latitude', models.DecimalField(max_digits=26, decimal_places=16)),
                ('longitude', models.DecimalField(max_digits=26, decimal_places=16)),
                ('planeOffset', models.DecimalField(max_digits=26, decimal_places=16)),
                ('pointDist', models.DecimalField(max_digits=26, decimal_places=16)),
                ('sportMode', models.IntegerField()),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='rid_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recordId', models.IntegerField(default=0)),
                ('table_name', models.CharField(max_length=16)),
            ],
        ),
    ]
