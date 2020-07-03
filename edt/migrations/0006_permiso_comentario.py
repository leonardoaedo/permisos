# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0005_auto_20151008_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='comentario',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
