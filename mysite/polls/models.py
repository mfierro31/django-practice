from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

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
