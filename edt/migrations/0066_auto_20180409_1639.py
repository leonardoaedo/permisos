# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0065_auto_20180409_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoLicencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='licencia',
            name='tipo',
            field=models.ForeignKey(to='edt.TipoLicencia', null=True),
        ),
    ]
