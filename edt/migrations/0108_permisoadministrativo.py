# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0107_auto_20220805_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermisoAdministrativo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('estado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, to='edt.Usuario', null=True)),
            ],
        ),
    ]
