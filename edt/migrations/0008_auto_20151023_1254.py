# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0007_auto_20151008_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventos_en_permisos',
            old_name='delta',
            new_name='deltafuncionario',
        ),
        migrations.AddField(
            model_name='eventos_en_permisos',
            name='deltainforme',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
