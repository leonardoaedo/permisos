# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0096_auto_20190307_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_permiso',
            name='nombre',
            field=models.CharField(max_length=256),
        ),
    ]
