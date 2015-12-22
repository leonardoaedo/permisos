# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0023_auto_20151209_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permiso',
            name='usuario',
        ),
        migrations.AddField(
            model_name='permiso',
            name='usuario',
            field=models.ForeignKey(related_name='usuario', default=1, to='edt.Usuario'),
            preserve_default=False,
        ),
    ]
