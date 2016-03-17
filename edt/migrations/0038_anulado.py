# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0037_auto_20160224_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anulado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anuladopor', models.ForeignKey(to='edt.Usuario')),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
    ]
