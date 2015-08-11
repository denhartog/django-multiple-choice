# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMultipleChoice', '0007_roletype_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionattempt',
            name='question',
        ),
    ]
