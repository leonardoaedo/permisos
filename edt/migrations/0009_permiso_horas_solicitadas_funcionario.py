# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0008_auto_20151023_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='horas_solicitadas_funcionario',
            field=models.CharField(default=0, max_length=32),
        ),
    ]
