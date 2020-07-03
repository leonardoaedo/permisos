# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0057_auto_20161223_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descontado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('cantidad', models.FloatField(default=0)),
                ('ingresadopor', models.ForeignKey(to='edt.Usuario')),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Devuelto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('cantidad', models.FloatField(default=0)),
                ('ingresadopor', models.ForeignKey(to='edt.Usuario')),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
    ]
