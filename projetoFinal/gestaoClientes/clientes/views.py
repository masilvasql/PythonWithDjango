from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import person
from .forms import PersonForm

@login_required
def personList(request):
    persons = person.objects.all()
    return render(request, 'person.html', { 'persons' : persons } )

@login_required
def personNew(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('personList')
    return render(request, 'person_form.html', {'form': form})

@login_required
def personUpdate(request, id):
    p = get_object_or_404(person, pk = id)
    form = PersonForm(request.POST or None,  request.FILES or None, instance = p)
    if form.is_valid():
        form.save()
        return redirect('personList')
    return render(request, 'person_form.html', {'form':form})
    
@login_required
def personDelete(request, id):
    p = get_object_or_404(person, pk = id)
    form = PersonForm(request.POST or None,  request.FILES or None, instance = p)
    if request.method == 'POST' :
        p.delete()
        return redirect('personList')
    return render(request, 'personDeleteConfirm.html', {'person':p})
