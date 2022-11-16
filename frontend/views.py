from datetime import date, datetime
from django.shortcuts import render, redirect
import requests
from api.models import *


def index(request):
    allpeople = requests.get('http://127.0.0.1:8000/api/people').json()
    people = {'people' : allpeople}

    if request.method == 'POST':
        persone = Person(
            name = request.POST.get('nome'),
            surname = request.POST.get('cognome'),
            friend = bool(request.POST.get('amico', False))

        )
        persone.save()
        return redirect('/')
    return render(request, 'index.html', people)

def instance(request, persons_id):
    instance = requests.get(f'http://127.0.0.1:8000/api/people/{persons_id}').json()
    id = instance['id']
    context = {'person' : instance, 'comments': Commentis.objects.filter(commented=id)}


    if request.method == 'POST':
        commento = Commentis(
            commented = Person.objects.get(id=id),
            mood = request.POST.get('mood'),
            comment = request.POST.get('comment'),
        )

        commento.save()
        return redirect(f'/persona/{id}')

 

    return render(request, 'single_person_view.html', context)