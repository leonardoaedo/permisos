# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0064_auto_20180409_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licencia',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='TLicencia',
        ),
    ]
