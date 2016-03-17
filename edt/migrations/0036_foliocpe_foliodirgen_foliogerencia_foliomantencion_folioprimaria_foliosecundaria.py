# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0035_auto_20160218_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='foliocpe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='foliodirgen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='foliogerencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='foliomantencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='folioprimaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='foliosecundaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
    ]
