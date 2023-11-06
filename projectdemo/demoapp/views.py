from django.shortcuts import render, redirect
from django.http import HttpResponse

from .form import PersonForm
from .models import Productdemo, Formdemo


# Create your views here.
def demo(request):
    product = Productdemo.objects.all()
    print(product)
    return render(request, 'index.html', {'product': product})


def form(request):
    if request.POST:
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('adress')
        person = Formdemo(name=name, age=age, address=address)
        person.save()
    return render(request, 'form.html')


def Form1(request):
    form1 = PersonForm()
    # print(form1)
    if request.method == 'POST':
        form1 = PersonForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('Form1')
    return render(request, 'form1.html', {'form1': form1})
