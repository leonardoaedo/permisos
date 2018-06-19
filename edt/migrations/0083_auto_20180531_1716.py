# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0082_auto_20180531_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reemplazolicencia',
            name='horaspagar',
            field=models.FloatField(default=0),
        ),
    ]
