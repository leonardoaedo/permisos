# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0042_auto_20160309_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='usuario',
            field=models.ForeignKey(blank=True, to='edt.Usuario', null=True),
        ),
    ]
