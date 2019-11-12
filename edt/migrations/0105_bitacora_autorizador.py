# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0104_bitacora_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacora',
            name='autorizador',
            field=models.ForeignKey(related_name='autorizador', to='edt.Usuario', null=True),
        ),
    ]
