from django.urls import path
from .views import*

urlpatterns=[
    path('',home,name='home'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('loginsave/',loginsave,name='loginsave'),
    path('dashboard/',dashboard,name='dashboard'),
    
    path('addsession/',addsession,name='addsession'),
] 