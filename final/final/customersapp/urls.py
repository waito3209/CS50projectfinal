from django.urls import path ,include

from . import views

urlpatterns = [
    path('/accounts/', include('django.contrib.auth.urls')),
    path('',views.mainpage,name='mainpage'),
    path("register/", views.register, name="register"),
]
