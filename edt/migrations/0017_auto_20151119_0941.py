# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0016_auto_20151106_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='sueldo',
            field=models.CharField(max_length=1, choices=[(b'C', b'Con goce de sueldo'), (b'S', b'Sin goce de sueldo')]),
        ),
    ]
