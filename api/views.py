from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

class showallpeople(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('surname')
    serializer_class = people

class showallcomments(viewsets.ModelViewSet):
    queryset = Commentis.objects.all().order_by('id')
    serializer_class = comments




    