from controlapp.models import *
from driverapp.models import *
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
import csv
with open('driver.csv') as f:
    reader=csv.reader(f)
    for i in reader:
        permission = Permission.objects.get(name='driver')
        a=User.objects.create_user(username=str(i[0]),password='test')

        a.save()
        a.user_permissions.add(permission)
        a.save()
        b=Driver(user=a,phonenumber=str(i[1]))
        b.save()