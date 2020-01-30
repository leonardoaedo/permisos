# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0099_tipo_ausencia_laboral'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ausencia_Laboral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.CharField(max_length=300, null=True, blank=True)),
                ('formacion', models.ForeignKey(blank=True, to='edt.Formacion', null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Tipo_Ausencia_Laboral',
            new_name='Motivo_Ausencia_Laboral',
        ),
        migrations.AddField(
            model_name='ausencia_laboral',
            name='motivo',
            field=models.ForeignKey(to='edt.Motivo_Ausencia_Laboral'),
        ),
        migrations.AddField(
            model_name='ausencia_laboral',
            name='reemplazante',
            field=models.ForeignKey(to='edt.Usuario'),
        ),
        migrations.AddField(
            model_name='ausencia_laboral',
            name='salida',
            field=models.ForeignKey(blank=True, to='edt.SalidaPedagogica', null=True),
        ),
    ]
