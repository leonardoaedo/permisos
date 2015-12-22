# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0022_auto_20151207_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permiso',
            name='usuario',
        ),
        migrations.AddField(
            model_name='permiso',
            name='usuario',
            field=models.ManyToManyField(related_name='usuario', to='edt.Usuario'),
        ),
    ]
