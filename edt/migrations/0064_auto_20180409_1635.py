# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0063_delete_treposo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tlicencia',
            name='nombre',
            field=models.TextField(max_length=150),
        ),
    ]
