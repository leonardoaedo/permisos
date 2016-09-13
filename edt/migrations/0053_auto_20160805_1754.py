# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0052_auto_20160708_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='permiso',
            name='estado',
            field=models.ForeignKey(blank=True, to='edt.Estado_Permiso', null=True),
        ),
    ]
