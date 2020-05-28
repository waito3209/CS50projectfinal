from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from controlapp.models import *
from driverapp.models  import *
from django.contrib.admin import widgets
class RegisterForm(forms.Form):

    username=forms.CharField(max_length=20)
    userpassword=forms.CharField(max_length=20)
    userphonenumber=forms.CharField(max_length=12)
    usercompany=forms.CharField(max_length=20,required = False)
    useremail=forms.EmailField(required=False)
class OrderForm(forms.Form):


    start_time =forms.TimeField()
    end_time =forms.TimeField(required=False)

    start_day =forms.DateField(input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    end_day =forms.DateField(required=False)

    start_place =forms.CharField(max_length=100)
    end_place =forms.CharField(required=False,max_length=100)

    specific_car=forms.ModelChoiceField(queryset=Cardata.objects.all(), empty_label="No going to specific", required=False)
    specific_driver=forms.ModelChoiceField(queryset=Driver.objects.all(), empty_label="No going to specific", required=False)
class EForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['start_time', 'end_time', 'start_day', 'end_day','start_place','end_place','driver','car','comment']
        widgets = {
            'start_day' : forms.DateInput(attrs={'type':'date'}),
            'end_day':forms.DateInput(attrs={'type':'date'}),
            'start_time':forms.TimeInput(attrs={'type':'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'})

        }