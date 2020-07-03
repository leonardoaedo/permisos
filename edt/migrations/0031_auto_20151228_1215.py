# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0030_auto_20151222_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='horas_solicitadas_funcionario',
            field=models.CharField(default=0, max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='motivo',
            field=models.ForeignKey(related_name='motivo', blank=True, to='edt.Motivo', null=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='tipo',
            field=models.ForeignKey(related_name='tipo_permiso', blank=True, to='edt.Tipo_Permiso', null=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='usuario',
            field=models.ForeignKey(related_name='usuario', blank=True, to='edt.Usuario', null=True),
        ),
    ]
