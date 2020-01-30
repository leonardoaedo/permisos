# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0100_auto_20190627_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='ausencia_laboral',
            name='funcionario',
            field=models.ForeignKey(blank=True, to='edt.Usuario', null=True),
        ),
        migrations.AlterField(
            model_name='ausencia_laboral',
            name='reemplazante',
            field=models.ForeignKey(related_name='usuario_reemplazante', default=162, to='edt.Usuario'),
        ),
    ]
