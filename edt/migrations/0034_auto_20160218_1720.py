# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0033_jefatura_correo3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='comentario',
            field=models.CharField(default=b'ingrese un comentario', max_length=32),
        ),
    ]
