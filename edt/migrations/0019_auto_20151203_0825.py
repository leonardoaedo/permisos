# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0018_auto_20151119_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='resolucion',
            name='respuesta',
            field=models.CharField(max_length=1, choices=[(b'A', b'Aprobado'), (b'R', b'Rechazado'), (b'N', b'Anulado')]),
        ),
    ]
