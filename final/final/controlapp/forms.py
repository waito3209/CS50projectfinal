from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class OrderProfileForm(forms.ModelForm):
    class Meta:
        model = Order
        fields='__all__'
        #Note that we didn't mention user field here.
        widgets = {
            'start_day': forms.DateInput(attrs={'type': 'date'}),
            'end_day': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'confirmed': forms.CheckboxInput(attrs={'class': 'confirmed'}),
        }
