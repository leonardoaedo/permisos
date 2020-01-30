# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0097_auto_20190312_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidapedagogica',
            name='fin',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='salidapedagogica',
            name='inicio',
            field=models.DateTimeField(null=True),
        ),
    ]
