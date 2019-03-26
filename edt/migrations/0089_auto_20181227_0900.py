# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0088_auto_20180725_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='devuelve_horas',
            field=models.CharField(default=b'N', max_length=1),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='sueldo',
            field=models.CharField(default=b'S', max_length=1),
        ),
    ]
