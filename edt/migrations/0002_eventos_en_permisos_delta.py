# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos_en_permisos',
            name='delta',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
