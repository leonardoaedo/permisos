# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0073_auto_20180416_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencia',
            name='horas',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='licencia',
            name='cantidad_dias',
            field=models.CharField(max_length=10),
        ),
    ]
