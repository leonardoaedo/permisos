# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0061_auto_20180403_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reposo', models.CharField(max_length=1, choices=[(b'M', b'Ma\xc3\xb1ana'), (b'T', b'Tarde'), (b'N', b'Noche')])),
                ('medico', models.CharField(max_length=250)),
                ('especialidad', models.CharField(max_length=250)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TLicencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TReposo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='licencia',
            name='tipo',
            field=models.ForeignKey(to='edt.TLicencia'),
        ),
        migrations.AddField(
            model_name='licencia',
            name='usuario',
            field=models.ForeignKey(to='edt.Usuario'),
        ),
    ]
