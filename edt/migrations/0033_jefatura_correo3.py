# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0032_auto_20151230_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='jefatura',
            name='correo3',
            field=models.EmailField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
