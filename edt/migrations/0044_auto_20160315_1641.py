# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0043_auto_20160315_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='horas',
            name='horas_aprobadas',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='horas',
            name='horas_rechazadas',
            field=models.FloatField(null=True),
        ),
    ]
