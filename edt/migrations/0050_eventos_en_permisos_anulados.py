# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0049_anulado_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos_en_Permisos_Anulados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deltainforme', models.CharField(max_length=32)),
                ('deltafuncionario', models.CharField(max_length=32)),
                ('evento', models.ForeignKey(to='edt.Evento')),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
    ]
