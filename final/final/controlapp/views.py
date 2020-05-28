from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
import json
from django.http import JsonResponse
from driverapp.models import *
from .forms import *

from django.views.generic import UpdateView
# Create your views here.
def mainpage(request):

    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:


            login(request, user)
        return redirect('/controlstaff')


    else:
        if not request.user.is_authenticated:
            return render(request, "login.html")

        return render(request, "staffhome.html")
def returndataO(request):
    tempdata={}
    temporder=None
    for i in Order.objects.all():
        if (i.confirmed==False ): #and (i.controllstaff.user==request.user):
            temporder=i
            break
    if temporder is None:
        return JsonResponse({'message':'no order'})
    tempdata['customer']=temporder.customer.user.username
    tempdata['customer_phone'] = temporder.customer.phonenumber
    tempdata['customer_email'] = temporder.customer.email
    tempdata['customer_company'] = temporder.customer.company

    tempdata['confirmed'] = temporder.confirmed
    tempdata['car']=str(temporder.car)
    if temporder.driver is not None:
        tempdata['driver']=str(temporder.driver)
        tempdata['driver_phone'] = str(temporder.driver.phonenumber)
    tempdata['start_time']=temporder.start_time
    tempdata['end_time']=temporder.end_time
    tempdata['start_day']=temporder.start_day
    tempdata['end_day']=temporder.end_day
    tempdata['start_place']=temporder.start_place
    tempdata['end_place']=temporder.end_place
    tempdata['comment']=str(temporder.comment)
    if temporder.controllstaff is not None:

        tempdata['controlstaff'] = temporder.controllstaff.user.username
    tempdata['pk'] = temporder.pk





    return JsonResponse(tempdata)
def getD(request):
    tempdata={'namelist':[]}
    for i in Driver.objects.all():
        tempdata['namelist'].append(str(i.user.username))
    return JsonResponse(tempdata)

    return JsonResponse()
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
@permission_required('controlapp.control')
def editform(request,num=1):
    # if request.user is not None and request.user.is_authenticated and request.user
    if request.method == 'POST':
        my_record = Order.objects.get(id=num)
        form = OrderProfileForm(request.POST,instance=my_record)
        if form.is_valid():
            my_record.customer=form.cleaned_data['customer']
            my_record.confirmed = form.cleaned_data['confirmed']
            my_record.car = form.cleaned_data['car']
            my_record.controllstaff = form.cleaned_data['controllstaff']
            my_record.start_time = form.cleaned_data['start_time']
            my_record.end_time = form.cleaned_data['end_time']
            my_record.start_day = form.cleaned_data['start_day']
            my_record.end_day = form.cleaned_data['end_day']
            my_record.start_place = form.cleaned_data['start_place']
            my_record.end_place = form.cleaned_data['end_place']
            my_record.comment = form.cleaned_data['comment']
            my_record.save()





    else:

        my_record = Order.objects.get(id=num)
        form = OrderProfileForm(instance=my_record)
    return render(request, 'editdata.html', {'form': form})




    return HttpResponse(str(num))