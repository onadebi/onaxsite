from django.db import models;
from datetime import datetime,timedelta;
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils import timezone;

class Question(models.Model):
    """Question model for the Poll app"""
    question_text = models.CharField(max_length=200,null=False)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self) -> str:
        return f"[{self.id}]-{self.question_text}"
    
    def was_published_recently(self)-> bool:
        return self.pub_date >= timezone.now() - timedelta(days=1)
    

class Choice(models.Model):
    """Choice model for the Poll app"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"[{self.id}]-{self.choice_text} - {self.votes} votes > from Question: {self.question}"
    

@receiver(post_migrate)
def _post_save_receiver(sender, **kwargs):
    if sender.name == 'poll':
        if not Question.objects.exists():
            Question.objects.create(question_text='What is your favorite color?', pub_date=timezone.now());
            Question.objects.create(question_text='Who is the president of Nigeria?', pub_date=timezone.now());
            Question.objects.create(question_text='How many continents are there on earth', pub_date=timezone.now());
            pass;
        if not Choice.objects.exists():
            q = Question.objects.all();
            Choice.objects.create(choice_text='Emerald', question=Question.objects.first())
            Choice.objects.create(choice_text='Emilokan', question=Question.objects.get(question_text='Who is the president of Nigeria?'))
            Choice.objects.create(choice_text='7', question=Question.objects.all()[2])   
