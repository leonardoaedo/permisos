# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0029_auto_20151222_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='permiso',
            field=models.ForeignKey(to='edt.Permiso', null=True),
        ),
    ]
