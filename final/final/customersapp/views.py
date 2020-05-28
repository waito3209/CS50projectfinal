import random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
import json
from .forms import *

# Create your views here.
def mainpage(request):

    if request.method == "POST":
        print('post')
        form = EForm(request.POST)
        if form.is_valid():
            print('valid')
            car = form.cleaned_data['car']
            driver = form.cleaned_data['driver']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            start_day = form.cleaned_data['start_day']
            end_day = form.cleaned_data['end_day']
            start_place = form.cleaned_data['start_place']
            end_place = form.cleaned_data['end_place']
            comment= form.cleaned_data['comment']
            random_idx = random.randint(0, Controllstaff.objects.count() - 1)
            random_object = Controllstaff.objects.all()[random_idx]
            print(request.user)
            print(type(request.user))
            tempcustomer=Customer.objects.get(user=request.user)
            print(tempcustomer)
            print(type(tempcustomer))
            tempOrder=Order(customer=tempcustomer,
                            car=car,
                            driver=driver,
                            start_time=start_time,
                            end_time=end_time,
                            start_day=start_day,
                            end_day=end_day,
                            start_place=start_place,
                            end_place=end_place,
                            controllstaff=random_object,
                            comment=comment)
            tempOrder.save()



            return HttpResponse("ok")
    else:
        form = EForm()




    return render(request, "customerhome.html", {"form":form})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            print('valid')
            username = form.cleaned_data['username']
            userpassword = form.cleaned_data['userpassword']
            userphonenumber = form.cleaned_data['userphonenumber']
            usercompany = form.cleaned_data['usercompany']
            useremail = form.cleaned_data['useremail']
            message=''
            if len(username)<5:
                message='length of username must longer than 5 '
            if len(userphonenumber)<8 or userphonenumber.isnumeric()!=True:
                message='invalid phone number'
            if message !='':
                return render(response, "register.html", {"form": form,"message":message})


            tempuser=User.objects.create_user(username,password=userpassword)
            tempcustomer=Customer(user=tempuser,
                                  phonenumber=userphonenumber,
                                  company=usercompany,
                                  email=useremail)
            tempcustomer.save()

        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})