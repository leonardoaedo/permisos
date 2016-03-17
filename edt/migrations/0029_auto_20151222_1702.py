# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0028_auto_20151222_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horas',
            name='permiso',
            field=models.ForeignKey(to='edt.Permiso', null=True),
        ),
    ]
