from django.contrib import admin
from .models import Productdemo
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
# Register your models here.
admin.site.register(Productdemo,ProductAdmin)
