# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0019_auto_20151203_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('actividad', models.ForeignKey(to='edt.Actividad')),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
                ('usuario', models.ForeignKey(to='edt.Usuario')),
            ],
        ),
    ]
