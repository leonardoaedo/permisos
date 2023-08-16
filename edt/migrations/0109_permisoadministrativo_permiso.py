# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0108_permisoadministrativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='permisoadministrativo',
            name='permiso',
            field=models.ForeignKey(default=3014, to='edt.Permiso'),
            preserve_default=False,
        ),
    ]
