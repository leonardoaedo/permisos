# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0011_auto_20151105_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='devuelve_horas',
            field=models.CharField(max_length=2, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
        ),
    ]
