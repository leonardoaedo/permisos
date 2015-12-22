# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0014_tipo_permiso'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='tipo',
            field=models.ForeignKey(related_name='tipo_permiso', default=1, to='edt.Tipo_Permiso'),
        ),
    ]
