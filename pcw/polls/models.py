from django.db import models
from django.utils import timesince, timezone
import datetime

# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now())

    def __str__(self):
        return self.content

    def publishedDate(self):
        return timesince.timesince(self.pub_date)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    content = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content