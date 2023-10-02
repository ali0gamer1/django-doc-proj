from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User



class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name = "users")

    def __str__(self):
        return self.choice_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add = True)
    choice = models.ManyToManyField(Choice, related_name = "choice")
    single_choice = models.BooleanField(default = True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text





