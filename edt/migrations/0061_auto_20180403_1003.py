# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0060_auto_20180309_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.ForeignKey(blank=True, to='edt.Estado', null=True),
        ),
    ]
