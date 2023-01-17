import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d") <= (self.pub_date).strftime("%Y-%m-%d") <= now.strftime("%Y-%m-%d")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
