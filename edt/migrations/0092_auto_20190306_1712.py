# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0091_formacion_salidapedagocica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='filename',
            field=models.CharField(default=b'usuario.nombre', max_length=100),
        ),
    ]
