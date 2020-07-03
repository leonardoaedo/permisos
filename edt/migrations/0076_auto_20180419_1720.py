# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0075_auto_20180419_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licencia',
            name='cantidad_dias',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='licencia',
            name='horas',
            field=models.FloatField(default=0),
        ),
    ]
