# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0013_auto_20151105_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
    ]
