# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_data1_speed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data1',
            name='id',
        ),
        migrations.AlterField(
            model_name='data1',
            name='timeStamp',
            field=models.DateTimeField(serialize=False, primary_key=True),
        ),
    ]
