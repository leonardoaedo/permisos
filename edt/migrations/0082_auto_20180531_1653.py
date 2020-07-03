# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0081_reemplazolicencia_ingresadopor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reemplazolicencia',
            old_name='horas',
            new_name='horaspagar',
        ),
        migrations.AddField(
            model_name='reemplazolicencia',
            name='horasreemplazo',
            field=models.FloatField(default=1),
        ),
    ]
