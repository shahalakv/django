from django.db import models

# Create your models here.
class Card(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
