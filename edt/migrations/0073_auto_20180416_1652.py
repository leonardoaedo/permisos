# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0072_licencia_cantidad_dias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licencia',
            name='cantidad_dias',
            field=models.CharField(max_length=2),
        ),
    ]
