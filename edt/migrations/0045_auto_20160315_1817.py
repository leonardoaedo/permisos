# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0044_auto_20160315_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='horas',
            name='horas_por_devolver',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_aprobadas',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_devueltas',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_rechazadas',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_solicitadas',
            field=models.FloatField(default=0),
        ),
    ]
