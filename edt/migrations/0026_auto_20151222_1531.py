# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0025_auto_20151222_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas',
            name='horas_devueltas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_solicitadas',
            field=models.IntegerField(),
        ),
    ]
