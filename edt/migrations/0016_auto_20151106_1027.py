# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0015_permiso_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='motivo',
            field=models.ForeignKey(related_name='motivo', to='edt.Motivo'),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='tipo',
            field=models.ForeignKey(related_name='tipo_permiso', to='edt.Tipo_Permiso'),
        ),
    ]
