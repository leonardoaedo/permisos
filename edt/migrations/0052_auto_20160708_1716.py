# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0051_revisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisor',
            name='primero',
            field=models.ForeignKey(related_name='primero', to='edt.Funcion'),
        ),
        migrations.AlterField(
            model_name='revisor',
            name='segundo',
            field=models.ForeignKey(related_name='segundo', to='edt.Funcion'),
        ),
        migrations.AlterField(
            model_name='revisor',
            name='tercero',
            field=models.ForeignKey(related_name='tercero', to='edt.Funcion'),
        ),
    ]
