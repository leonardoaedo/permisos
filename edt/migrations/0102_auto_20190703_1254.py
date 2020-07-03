# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0101_auto_20190701_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='ausencia_laboral',
            name='fin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ausencia_laboral',
            name='inicio',
            field=models.DateTimeField(null=True),
        ),
    ]
