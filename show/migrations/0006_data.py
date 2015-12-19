# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0005_auto_20151219_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('timeStamp', models.DateTimeField(serialize=False, primary_key=True)),
                ('altitude', models.FloatField()),
                ('deviceX', models.FloatField()),
                ('deviceY', models.FloatField()),
                ('deviceZ', models.FloatField()),
                ('isIntegerKM', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('pointDist', models.FloatField()),
                ('speed', models.FloatField()),
                ('Mode', models.ForeignKey(to='show.mode')),
            ],
        ),
    ]
