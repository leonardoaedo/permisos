# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0056_horas_horas_pendientes_por_aprovar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horas',
            old_name='horas_pendientes_por_aprovar',
            new_name='horas_pendientes_por_aprobar',
        ),
    ]
