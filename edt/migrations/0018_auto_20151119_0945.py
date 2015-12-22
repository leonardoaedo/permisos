# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0017_auto_20151119_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='reemplazante',
            field=models.ForeignKey(related_name='reemplazante', blank=True, to='edt.Usuario', null=True),
        ),
    ]
