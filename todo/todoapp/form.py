from django.forms import ModelForm

from.models import Card


class PersonForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
