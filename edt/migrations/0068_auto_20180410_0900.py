# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0067_auto_20180409_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licencia',
            old_name='usuario',
            new_name='funcionario',
        ),
    ]
