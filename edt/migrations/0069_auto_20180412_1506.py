# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0068_auto_20180410_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspecialidadMedica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='licencia',
            name='especialidad',
            field=models.ForeignKey(to='edt.EspecialidadMedica'),
        ),
    ]
