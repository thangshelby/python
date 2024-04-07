
# Create your models here.
from django.db import models
import datetime
# from django.db.utils import timezone
# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=20)
    mobile_number = models.PositiveIntegerField()
    employee_title = models.CharField(max_length=10)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() 


class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CACADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text
