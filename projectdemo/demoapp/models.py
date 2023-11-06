from django.db import models


# Create your models here.
class Productdemo(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.CharField(max_length=2500)


class Formdemo(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.CharField(max_length=250)
