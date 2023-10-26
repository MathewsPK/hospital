from django import forms
from .models import appointments

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = appointments
        fields = '__all__'
