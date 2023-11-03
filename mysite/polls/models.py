from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """ 
    Django automatically adds a primary key field for you in your models if you don't specify one yourself,
    so, here, ForeignKey will reference a unique primary key, we just don't see it here in the code, but it will be
    created once these tables are created in the database.  The default primary key data type is located in the bottom
    of mysite/settings.py
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
