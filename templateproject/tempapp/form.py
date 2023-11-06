from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from tempapp.models import Customer
class CustomerForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ('name','username','phone','occupation','password1','password2')


class PhysicianForm(UserCreationForm):

    class Meta:
        model = Customer
        fields =('name','username','address','phone','password1','password2')