# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0055_horas_horas_sin_recuperacion_con_goce'),
    ]

    operations = [
        migrations.AddField(
            model_name='horas',
            name='horas_pendientes_por_aprovar',
            field=models.FloatField(default=0),
        ),
    ]
