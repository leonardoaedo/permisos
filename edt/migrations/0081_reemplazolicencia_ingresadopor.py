# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0080_reemplazolicencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='reemplazolicencia',
            name='ingresadopor',
            field=models.ForeignKey(related_name='usuario_sesion', default=1, to='edt.Usuario'),
            preserve_default=False,
        ),
    ]
