
from customersapp.models import *
from driverapp.models import *
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Controllstaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254,blank=True)
    company = models.CharField(max_length=50,blank=True)
    phonenumber =models.CharField(max_length=11)
    def __str__(self):
        return self.user.username
class Cardata(models.Model):
    carnumber = models.CharField(max_length=6,primary_key=True)
    carname = models.TextField()
    color = models.CharField(max_length=10,blank=True)
    seatnumber = models.SmallIntegerField()
    price_hour = models.SmallIntegerField(blank=True)
    def __str__(self):
        return self.carname+'  '+self.color+ ' ' +' with '+str(self.seatnumber) +' seat  $'+str(self.price_hour)+ ' per hours'
class Order(models.Model):


    customer= models.ForeignKey(Customer, on_delete=models.CASCADE,unique=False)
    confirmed=models.BooleanField(default=False,blank=True)
    car = models.ForeignKey(Cardata, on_delete=models.CASCADE,blank=True,null=True)

    controllstaff = models.ForeignKey(Controllstaff, on_delete=models.CASCADE,blank=True,null=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,blank=True,null=True)

    start_time = models.TimeField()
    end_time = models.TimeField(blank=True,null=True)

    start_day = models.DateField()
    end_day = models.DateField(blank=True,null=True)

    start_place = models.CharField(max_length=100)
    end_place = models.CharField(blank=True,max_length=100)
    comment = models.TextField(blank=True)
    def __str__(self):
        tempstring=''
        if self.customer is not None:
            tempstring+= 'Constomer : '+self.customer.user.username
        if self.driver is not None:
            tempstring += 'driver : ' + self.driver.user.username
        if self.controllstaff is not None:
            tempstring += 'controllstaff : ' + self.controllstaff.user.username
        return tempstring+' '+str(self.start_day)