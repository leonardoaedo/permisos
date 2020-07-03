# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0066_auto_20180409_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoReposo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=2, choices=[(b'M', b'Ma\xc3\xb1ana'), (b'T', b'Tarde'), (b'N', b'Noche'), (b'TT', b'Total')])),
            ],
        ),
        migrations.AlterField(
            model_name='licencia',
            name='reposo',
            field=models.ForeignKey(to='edt.TipoReposo', null=True),
        ),
    ]
