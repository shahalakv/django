from django.urls import path
from .import views


urlpatterns = [
    path('', views.demo, name='demo'),
    path('form/', views.form, name='form'),
    path('form1/', views.Form1, name='Form1')


]

