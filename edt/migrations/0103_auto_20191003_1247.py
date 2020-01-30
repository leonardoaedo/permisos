# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0102_auto_20190703_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolucion',
            name='respuesta',
            field=models.CharField(max_length=1, choices=[(b'A', b'Aprobado'), (b'R', b'Rechazado'), (b'N', b'Anulado'), (b'M', b'Modificado')]),
        ),
    ]
