from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.
def index(request):
    return HttpResponse("helloworld")
def create(request):
    return render(request,'index.html')
def edit(request):
    return render(request,'edit.html')
def about(request):
    student={
    'name':'shahala',
    'year':'2015',
    }
    return render(request,'index.html',student)
# def about(request):
#     student_details={'students':[
#         {
#             'name':'anika',
#             'year':'2015',
#         },
#         {
#             'name':'anu',
#             'year':'2014',
#         },
#     ]}
#     return render(request,'index.html',student_details)

def demo(request):
    product1=product.objects.all()
    return render(request,'index.html',{'product1':product1})

def card(request):
    product2=product.objects.all()
    return render(request,'card.html',{'product2':product2})
