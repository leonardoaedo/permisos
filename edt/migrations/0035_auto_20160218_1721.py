# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0034_auto_20160218_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='comentario',
            field=models.CharField(default=b'Sin comentario', max_length=32),
        ),
    ]
