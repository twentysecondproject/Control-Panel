from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class people(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'surname', 'friend')

class comments(serializers.ModelSerializer):
    class Meta:
        model = Commentis
        fields = ('id', 'commented', 'mood', 'comment', 'date')


