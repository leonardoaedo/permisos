# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0103_auto_20191003_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacora',
            name='comentario',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
