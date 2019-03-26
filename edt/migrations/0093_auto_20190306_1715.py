# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0092_auto_20190306_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='filename',
            field=models.CharField(default=b'edt.Usuario', max_length=100),
        ),
    ]
