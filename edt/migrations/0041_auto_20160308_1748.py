# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0040_auto_20160301_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='comentario',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='motivo',
            field=models.ForeignKey(related_name='motivo', default=1, to='edt.Motivo'),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='tipo',
            field=models.ForeignKey(related_name='tipo_permiso', default=1, to='edt.Tipo_Permiso'),
        ),
    ]
