from django.forms import ModelForm

from demoapp.models import Formdemo


class PersonForm(ModelForm):
    class Meta:
        model = Formdemo
        fields = '__all__'
