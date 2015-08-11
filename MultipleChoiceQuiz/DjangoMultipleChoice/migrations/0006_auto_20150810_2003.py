# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMultipleChoice', '0005_auto_20150810_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('question', models.ForeignKey(to='DjangoMultipleChoice.Question')),
                ('question_answer', models.ForeignKey(to='DjangoMultipleChoice.QuestionAnswer')),
            ],
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('quiz', models.ForeignKey(to='DjangoMultipleChoice.Quiz')),
                ('role', models.ForeignKey(to='DjangoMultipleChoice.Role')),
            ],
        ),
        migrations.AddField(
            model_name='questionattempt',
            name='quiz_attempt',
            field=models.ForeignKey(to='DjangoMultipleChoice.QuizAttempt'),
        ),
    ]
