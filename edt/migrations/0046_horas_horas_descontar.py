# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0045_auto_20160315_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='horas',
            name='horas_descontar',
            field=models.FloatField(default=0),
        ),
    ]
