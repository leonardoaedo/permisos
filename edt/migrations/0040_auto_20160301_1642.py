# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0039_auto_20160229_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolucion',
            name='razon',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
