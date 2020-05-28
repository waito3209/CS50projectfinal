from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254,blank=True)
    company = models.CharField(max_length=50,blank=True)
    phonenumber =models.CharField(max_length=11)
    def __str__(self):
        return self.user.username
