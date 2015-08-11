# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMultipleChoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.TextField()),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('update_date', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.TextField()),
                ('correct', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('update_date', models.DateTimeField(verbose_name=b'date updated')),
                ('question', models.ForeignKey(to='DjangoMultipleChoice.Question')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='intro_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(to='DjangoMultipleChoice.Quiz'),
        ),
    ]
