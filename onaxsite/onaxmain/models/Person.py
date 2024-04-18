from django.db import models;
from datetime import datetime;

class Person(models.Model):
    id :int = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=100,null=False,unique=True)
    date_registered = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'Person';
        db_table_description = 'This table contains the details of all persons in the system';


class Musician(models.Model):
    first_name = models.CharField(max_length=50,null=False,error_messages={'required':'First name is required'})
    last_name = models.CharField(max_length=50,null=False)
    instrument = models.CharField(max_length=100);
    gender = models.CharField(max_length=5, choices={'M':'Male','F': 'Female','O':'Other'}, default='M');

    class Meta:
        db_table = 'Musician';
        db_table_description = 'This table contains the details of all musicians in the system';


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=False)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    class Meta:
        db_table = 'Album';
        db_table_description = 'This table contains the details of all albums in the system';