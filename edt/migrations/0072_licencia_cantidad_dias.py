# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0071_auto_20180413_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencia',
            name='cantidad_dias',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
