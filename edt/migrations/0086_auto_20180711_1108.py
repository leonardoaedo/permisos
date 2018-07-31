# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0085_remove_reemplazolicencia_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licencia',
            name='cantidad_dias',
            field=models.IntegerField(default=0),
        ),
    ]
