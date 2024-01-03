from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Customer(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=250, null=True)
