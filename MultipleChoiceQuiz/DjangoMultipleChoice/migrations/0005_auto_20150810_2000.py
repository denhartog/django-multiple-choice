# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMultipleChoice', '0004_name_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.OneToOneField(to='DjangoMultipleChoice.Name'),
        ),
        migrations.AddField(
            model_name='role',
            name='person',
            field=models.ForeignKey(to='DjangoMultipleChoice.Person'),
        ),
        migrations.AddField(
            model_name='role',
            name='role_type',
            field=models.ForeignKey(to='DjangoMultipleChoice.RoleType'),
        ),
    ]
