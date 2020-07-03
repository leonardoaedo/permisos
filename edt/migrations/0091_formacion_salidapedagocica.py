# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0090_auto_20181227_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('inicio', models.DateTimeField(null=True)),
                ('fin', models.DateTimeField(null=True)),
                ('ubicacion', models.CharField(max_length=150)),
                ('agno', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='SalidaPedagocica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('ubicacion', models.CharField(max_length=150)),
                ('agno', models.CharField(max_length=4)),
            ],
        ),
    ]
