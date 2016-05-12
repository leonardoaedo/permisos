# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0047_anulado_motivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='horas',
            name='horas_descontadas',
            field=models.FloatField(default=0),
        ),
    ]
