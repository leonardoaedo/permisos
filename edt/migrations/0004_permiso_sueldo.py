# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0003_auto_20150910_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='sueldo',
            field=models.CharField(default=1, max_length=1, choices=[(b'S', b'SI'), (b'N', b'NO')]),
            preserve_default=False,
        ),
    ]
