from email.policy import default
from django.db import models
from datetime import datetime    

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    friend = models.BooleanField(default=True)

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    def __int__(self):
        return self.id

class Commentis(models.Model):
    id = models.AutoField(primary_key=True)
    commented = models.ForeignKey(Person, models.CASCADE)
    mood = models.CharField(max_length=60)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id 
