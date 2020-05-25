# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_auto_20200518_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='added_by',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
