# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0012_auto_20151105_1241'),
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
            field=models.CharField(max_length=1, choices=[(b'S', b'SI'), (b'N', b'NO')]),
        ),
    ]
