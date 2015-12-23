# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.RemoveField(
            model_name='news',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='news',
            name='photo',
        ),
    ]
