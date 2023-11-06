from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from tempapp.models import Customer
from tempapp.form import CustomerForm, PhysicianForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


# def cust_reg(request):
#     form = CustomerForm()
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cust_reg')
#     return render(request, 'cust_reg.html', {'form': form})


def cust_reg(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            return redirect('cust_reg')
    return render(request, 'cust_reg.html', {'form': form})
def phy_reg(request):
    form = PhysicianForm()
    if request.method =='POST':
        form = PhysicianForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_physician = True
            user.save()
        return redirect('phy_reg')
    return render(request, 'phy_reg.html', {'form': form})



def admin_page(request):
    return render(request, 'admin_page.html')

def customer_page(request):
    return render(request, 'customer_page.html')

def physician_page(request):
    return render(request, 'physician_page.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_customer:
                return redirect('customer_page')
            elif user.is_physician:
                return redirect('physician_page')
        else:
            messages.error(request,'invalid')
    return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('index')