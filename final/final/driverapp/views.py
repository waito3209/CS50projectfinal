from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
import json

from controlapp.models import *
# Create your views here.
def mainpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/driverstaff/')

        return render(request, "logindriver.html",{'message':'failtologin'})
    else:
        if not request.user.is_authenticated:
            return render(request, "logindriver.html")

        return render(request, "driverhome.html")


from django.shortcuts import render

# Create your views here.
def getDS(request):
    if request.method=='POST':
        drivername= request.POST['drivername']
        date = request.POST['date']
        print(drivername)
        print(date)
        alldata=[]
        tempdriver=Driver.objects.get(user=User.objects.get(username=drivername))

        if Order.objects.filter(driver=tempdriver,start_day=date) is not None:

            for i in Order.objects.filter(driver=tempdriver,start_day=date).all():
                print(tempdriver)
                tempdata={}
                tempdata['customer'] = str(i.customer.user.username)
                tempdata['customer phone']=str(i.customer.phonenumber)
                if i.controllstaff is not None:
                    tempdata['control_staff_name']=str(i.controllstaff.user.username)
                    tempdata['control_staff_phone'] =str(i.controllstaff.phonenumber)
                tempdata['confirmed'] = str(i.confirmed)
                tempdata['car'] = str(i.car)
                tempdata['driver'] = str(i.driver)
                tempdata['start_time'] = str(i.start_time)
                tempdata['end_time'] = str(i.end_time)
                tempdata['start_day'] = str(i.start_day)
                tempdata['end_day'] = str(i.end_day)
                tempdata['start_place'] =str(i.start_place)
                tempdata['end_place'] = str(i.end_place)
                tempdata['comment'] = str(i.comment)

                alldata.append(tempdata)
        print(alldata)
        return JsonResponse({'alldata':alldata})
    else:
        HttpResponseForbidden()
