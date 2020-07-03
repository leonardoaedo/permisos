# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0083_auto_20180531_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencia',
            name='ingresadopor',
            field=models.ForeignKey(related_name='ingresado_por', default=1, to='edt.Usuario'),
            preserve_default=False,
        ),
    ]
