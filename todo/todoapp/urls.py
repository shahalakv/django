from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.stud_view, name="stud_view"),
    path('stud_update/<int:up>', views.stud_update, name='stud_update'),
    path('stud_delete/<int:dl>', views.stud_delete, name='stud_delete')

]
