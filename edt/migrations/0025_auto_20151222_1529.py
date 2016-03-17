# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0024_auto_20151209_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas',
            name='horas_devueltas',
            field=models.IntegerField(default=0, max_length=32),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_solicitadas',
            field=models.IntegerField(default=0, max_length=32),
        ),
    ]
