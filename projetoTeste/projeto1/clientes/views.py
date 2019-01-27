from django.shortcuts import render
from .models import person


def personList(request):
    persons = person.objects.all()
    return render(request, 'person.html', { 'persons' : persons } )
