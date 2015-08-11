# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMultipleChoice', '0003_auto_20150810_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=255)),
                ('middle', models.CharField(max_length=255, null=True)),
                ('last', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.ForeignKey(to='DjangoMultipleChoice.Name')),
            ],
        ),
    ]
