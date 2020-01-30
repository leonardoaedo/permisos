# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0098_auto_20190617_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Ausencia_Laboral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
    ]
