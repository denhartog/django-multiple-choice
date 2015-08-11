# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMultipleChoice', '0006_auto_20150810_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='roletype',
            name='type',
            field=models.CharField(default=b'B', max_length=1, choices=[(b'B', b'Basic'), (b'T', b'Teacher'), (b'S', b'Student'), (b'P', b'Principal')]),
        ),
    ]
