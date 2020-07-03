# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0070_licencia_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licencia',
            name='fin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='licencia',
            name='inicio',
            field=models.DateTimeField(),
        ),
    ]
