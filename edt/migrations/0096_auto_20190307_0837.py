# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0095_auto_20190306_1717'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SalidaPedagocica',
            new_name='SalidaPedagogica',
        ),
    ]
