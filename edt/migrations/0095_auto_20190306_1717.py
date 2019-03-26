# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0094_auto_20190306_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='filename',
            field=models.CharField(max_length=100),
        ),
    ]
