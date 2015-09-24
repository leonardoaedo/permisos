# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0002_eventos_en_permisos_delta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='apellido1',
        ),
        migrations.AddField(
            model_name='usuario',
            name='apellido2',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
