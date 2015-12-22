# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0020_bitacora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('horas', models.CharField(default=0, max_length=32)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
                ('usuario', models.ForeignKey(to='edt.Usuario')),
            ],
        ),
    ]
