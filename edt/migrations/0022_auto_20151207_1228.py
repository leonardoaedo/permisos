# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0021_horas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horas',
            old_name='horas',
            new_name='horas_devueltas',
        ),
        migrations.AddField(
            model_name='horas',
            name='horas_solicitadas',
            field=models.CharField(default=0, max_length=32),
        ),
    ]
