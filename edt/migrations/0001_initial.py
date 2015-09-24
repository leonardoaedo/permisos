# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Centrocosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=100)),
                ('docfile', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('snippet', models.CharField(max_length=150, blank=True)),
                ('body', models.TextField(max_length=10000, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(blank=True)),
                ('remind', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Estadoaprovacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Estamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_carga', models.DateTimeField(auto_now_add=True, null=True)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos_en_Permisos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_evento', models.ForeignKey(to='edt.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Jefatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('correo1', models.EmailField(max_length=128)),
                ('correo2', models.EmailField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('horas_solicitadas', models.CharField(default=0, max_length=32)),
                ('devuelve_horas', models.CharField(max_length=1, choices=[(b'S', b'SI'), (b'N', b'NO')])),
                ('documento_adjunto', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=1, choices=[(b'A', b'Aprobado'), (b'R', b'Rechazado')])),
                ('razon', models.CharField(max_length=32, null=True, blank=True)),
                ('fecha_resolucion', models.DateField(auto_now_add=True)),
                ('permiso', models.ForeignKey(to='edt.Permiso')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('nivel_acceso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut', models.CharField(max_length=32)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=32)),
                ('apellido', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('correo', models.EmailField(max_length=128)),
                ('horas_contratadas', models.CharField(max_length=32)),
                ('fecha_nac', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('telefono', models.CharField(max_length=32, null=True, blank=True)),
                ('foto', models.FileField(null=True, upload_to=b'', blank=True)),
                ('cargo', models.ForeignKey(to='edt.Cargo')),
                ('contrato', models.ForeignKey(to='edt.Contrato')),
                ('estamento', models.ForeignKey(to='edt.Estamento')),
                ('funcion', models.ForeignKey(to='edt.Funcion')),
                ('jefatura', models.ForeignKey(to='edt.Jefatura')),
                ('nacionalidad', models.ForeignKey(to='edt.Nacionalidad')),
                ('rol', models.ForeignKey(to='edt.Rol')),
                ('sexo', models.ForeignKey(to='edt.Sexo')),
            ],
        ),
        migrations.AddField(
            model_name='resolucion',
            name='resolutor',
            field=models.ForeignKey(to='edt.Usuario'),
        ),
        migrations.AddField(
            model_name='permiso',
            name='reemplazante',
            field=models.ForeignKey(related_name='reemplazante', to='edt.Usuario'),
        ),
        migrations.AddField(
            model_name='permiso',
            name='usuario',
            field=models.ForeignKey(related_name='usuario', to='edt.Usuario'),
        ),
        migrations.AddField(
            model_name='eventos_en_permisos',
            name='numero_permiso',
            field=models.ForeignKey(to='edt.Permiso'),
        ),
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(related_name='edt_user', to='edt.Usuario'),
        ),
        migrations.AddField(
            model_name='entry',
            name='creator',
            field=models.ForeignKey(blank=True, to='edt.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='usuario',
            field=models.ForeignKey(to='edt.Usuario', null=True),
        ),
    ]
