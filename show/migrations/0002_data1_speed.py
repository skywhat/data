# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data1',
            name='speed',
            field=models.DecimalField(default=0, max_digits=26, decimal_places=16),
            preserve_default=False,
        ),
    ]
