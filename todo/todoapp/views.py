from django.shortcuts import render, redirect
from django.http import HttpResponse

from todoapp.form import PersonForm
from todoapp.models import Card


# Create your views here.
def index(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('stud_view')

    return render(request, 'index.html', {"form": form})

def stud_view(request):
    new = Card.objects.all()
    return render(request, 'view.html', {"new": new})

def stud_update(request, up):
    taskupdate = Card.objects.get(id=up)
    updateform = PersonForm(instance=taskupdate)
    if request.method == 'POST':
        updateform=PersonForm(request.POST,instance=taskupdate)
        if updateform.is_valid():
            updateform.save()
            return redirect("stud_view")
    return render(request, "update.html", {"updateform": updateform})
def stud_delete(request, dl):
    taskdelete = Card.objects.get(id=dl)
    taskdelete.delete()
    return redirect("stud_view")