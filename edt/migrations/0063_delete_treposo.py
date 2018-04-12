# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0062_auto_20180409_1630'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TReposo',
        ),
    ]
