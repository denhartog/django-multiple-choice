from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=255)
    intro_text = models.TextField(null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True, null=True)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    question_text = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True, null=True)

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.TextField()
    correct = models.BooleanField(default=False)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True, null=True)

class Name(models.Model):
    first = models.CharField(max_length=255)
    middle = models.CharField(max_length=255, null=True)
    last = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True, null=True)

class Person(models.Model):
    name = models.OneToOneField(Name)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True, null=True)

class RoleType(models.Model):
    type = (
        ('T', 'Teacher'),
        ('S', 'Student'),
        ('P', 'Principal')
    )

class Role(models.Model):
    person = models.ForeignKey(Person)
    role_type = models.ForeignKey(RoleType)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True, null=True)

class QuizAttempt(models.Model):
    role = models.ForeignKey(Role)
    quiz = models.ForeignKey(Quiz)
    create_date = models.DateTimeField()

class QuestionAttempt(models.Model):
    quiz_attempt = models.ForeignKey(QuizAttempt)
    question = models.ForeignKey(Question)
    question_answer = models.ForeignKey(QuestionAnswer)
    create_date = models.DateTimeField()



