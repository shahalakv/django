from django.contrib.auth.forms import UserCreationForm
from vacapp.models import Vaccination, Hospital, Vaccine, Appointment, Reportcard, Complaint, Book_Appointment
from django import forms

class UserForm(UserCreationForm):

    class Meta:
        model = Vaccination
        fields = ('username', 'password1', 'password2', 'address', 'child_name', 'child_age', 'gender')


class NurseForm(UserCreationForm):

    class Meta:
        model = Vaccination
        fields = ('username', 'password1', 'password2', 'name', 'email', 'address', 'hospital')

class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = ('name', 'place', 'email', 'contact')

class VaccineForm(forms.ModelForm):

    class Meta:
        model = Vaccine
        fields = ('vaccine_name', 'type', 'description')

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('hospital', 'date', 'start_time', 'end_time')

class ReportcardForm(forms.ModelForm):

    class Meta:
        model =Reportcard
        fields = ('patient_name', 'vaccine')

class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ('user', 'subject', 'complaint', 'date')

class Book_AppointmentForm(forms.ModelForm):

    class Meta:
        model = Book_Appointment
        fields = ('schedule', 'vaccine_name', 'vaccine', 'status')