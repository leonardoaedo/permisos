# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0053_auto_20160805_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='horas',
            name='horas_descontar_acumuladas',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='horas',
            name='horas_por_devolver_acumuladas',
            field=models.FloatField(default=0),
        ),
    ]
