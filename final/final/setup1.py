from controlapp.models import *
from driverapp.models import *
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
import csv
with open("cardata.csv") as f:
    reader = csv.reader(f)
    for i in reader:
        #print(i[1])

        a = Cardata(carnumber=str(i[1]), carname=str(i[0]),color=str(i[2]),price_hour=int(float(i[3])),seatnumber=int(i[4]))
        a.save()
