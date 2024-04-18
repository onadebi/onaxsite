from django.db import models;
from datetime import datetime,timedelta;
from django.utils import timezone;

class Question(models.Model):
    question_text = models.CharField(max_length=200,null=False)
    pub_date = models.DateTimeField('date published', default=datetime.now())

    def __str__(self) -> str:
        return f"[{self.id}]-{self.question_text}"
    
    def was_published_recently(self)-> bool:
        return self.pub_date >= timezone.now() - timedelta(days=1)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"[{self.id}]-{self.choice_text} - {self.votes} votes"
    