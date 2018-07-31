# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0086_auto_20180711_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='reemplazolicencia',
            name='fecha_ingreso',
            field=models.DateField(default=b'2018-01-01'),
        ),
    ]
