# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0059_sindicato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='reemplazante',
            field=models.ForeignKey(related_name='reemplazante', default=162, to='edt.Usuario'),
        ),
    ]
