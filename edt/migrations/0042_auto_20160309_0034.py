# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0041_auto_20160308_1748'),
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
