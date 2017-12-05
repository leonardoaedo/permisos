# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0058_descontado_devuelto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sindicato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(max_length=128)),
                ('usuario', models.ForeignKey(to='edt.Usuario')),
            ],
        ),
    ]
