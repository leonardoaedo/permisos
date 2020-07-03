# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0036_foliocpe_foliodirgen_foliogerencia_foliomantencion_folioprimaria_foliosecundaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motivo',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
