# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0046_horas_horas_descontar'),
    ]

    operations = [
        migrations.AddField(
            model_name='anulado',
            name='motivo',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
