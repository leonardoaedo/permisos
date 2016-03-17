# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0026_auto_20151222_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas',
            name='horas_devueltas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_solicitadas',
            field=models.FloatField(),
        ),
    ]
