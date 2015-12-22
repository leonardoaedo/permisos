# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0004_permiso_sueldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='permiso',
            name='motivo',
            field=models.ForeignKey(related_name='motivo', default=b'1', to='edt.Motivo'),
        ),
    ]
