# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0006_permiso_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolucion',
            name='razon',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
