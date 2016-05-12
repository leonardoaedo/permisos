# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0048_horas_horas_descontadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='anulado',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
