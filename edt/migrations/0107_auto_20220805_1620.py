# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0106_auto_20200218_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcion',
            options={'ordering': ('nombre',)},
        ),
        migrations.AlterModelOptions(
            name='licencia',
            options={'ordering': ('-fin',)},
        ),
    ]
