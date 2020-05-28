from django.urls import path ,include

from . import views

urlpatterns = [

    path('',views.mainpage,name='drivermainpage'),
    path('getDS',views.getDS,name='drivergetown')

]
