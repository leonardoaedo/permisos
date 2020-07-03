# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0054_auto_20161220_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='horas',
            name='horas_sin_recuperacion_con_goce',
            field=models.FloatField(default=0),
        ),
    ]
