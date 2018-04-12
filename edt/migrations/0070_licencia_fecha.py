# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0069_auto_20180412_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencia',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
