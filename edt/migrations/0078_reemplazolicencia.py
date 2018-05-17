# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0077_auto_20180419_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReemplazoLicencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horas', models.FloatField(default=1)),
                ('pago', models.CharField(max_length=2, choices=[(b'SI', b'Se Paga'), (b'NO', b'No Se Paga')])),
                ('licencia', models.ForeignKey(to='edt.Licencia')),
                ('reemplazante', models.ForeignKey(to='edt.Usuario')),
            ],
        ),
    ]
