# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20151126_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rid_table',
            name='id',
        ),
        migrations.AlterField(
            model_name='rid_table',
            name='recordId',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
    ]
