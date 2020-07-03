# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0050_eventos_en_permisos_anulados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estamento', models.ForeignKey(to='edt.Estamento')),
                ('primero', models.ForeignKey(related_name='primero', to='edt.Usuario')),
                ('segundo', models.ForeignKey(related_name='segundo', to='edt.Usuario')),
                ('tercero', models.ForeignKey(related_name='tercero', to='edt.Usuario')),
            ],
        ),
    ]
