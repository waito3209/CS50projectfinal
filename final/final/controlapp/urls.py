from django.urls import path ,include

from . import views

urlpatterns = [

    path('',views.mainpage,name='staffmainpage'),
    path('getO',views.returndataO,name='getO'),
    path('getD',views.getD,name='getD'),
    path('getDS',views.getDS,name='getDS'),
    path('edit/<int:num>/', views.editform,name='editform'),
    path('edit', views.editform,name='editform'),
]
