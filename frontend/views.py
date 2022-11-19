from django.shortcuts import render, redirect
from api.models import *


def index(request):
    people = {'people' : Person.objects.all()}

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
    context = {'person' : Person.objects.get(id=persons_id), 'comments': Commentis.objects.filter(commented=persons_id)}


    if request.method == 'POST':
        commento = Commentis(
            commented = Person.objects.get(id=persons_id),
            mood = request.POST.get('mood'),
            comment = request.POST.get('comment'),
        )

        commento.save()
        return redirect(f'/persona/{id}')

 

    return render(request, 'single_person_view.html', context)