# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0087_reemplazolicencia_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reemplazolicencia',
            name='fecha_ingreso',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
