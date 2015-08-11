# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMultipleChoice', '0002_auto_20150810_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='create_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
