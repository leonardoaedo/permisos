# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0084_licencia_ingresadopor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reemplazolicencia',
            name='pago',
        ),
    ]
