# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0027_auto_20151222_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas',
            name='horas_devueltas',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='horas',
            name='horas_solicitadas',
            field=models.FloatField(null=True),
        ),
    ]
