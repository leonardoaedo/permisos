# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0089_auto_20181227_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='devuelve_horas',
            field=models.CharField(max_length=1, choices=[(b'S', b'SI'), (b'N', b'NO')]),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='sueldo',
            field=models.CharField(max_length=1, choices=[(b'C', b'Con goce de sueldo'), (b'S', b'Sin goce de sueldo')]),
        ),
    ]
