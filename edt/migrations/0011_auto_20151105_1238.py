# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0010_auto_20151029_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='devuelve_horas',
            field=models.CharField(max_length=1, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='sueldo',
            field=models.CharField(max_length=1, choices=[(b'SI', b'SI'), (b'NO', b'NO')]),
        ),
    ]
