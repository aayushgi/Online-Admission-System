from django.urls import path
from .views import*

urlpatterns=[
    path('',home,name='home'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('loginsave/',loginsave,name='loginsave'),
    path('dashboard/',dashboard,name='dashboard'),
    
    path('addsession/',addsession,name='addsession'),
    path('showsession/',showsession,name='showsession'),
    path('deletesession/<int:id>/',deletesession,name='deletesession'),
    path('addcourse/',addcourse,name='addcourse'),
    path('showcourse/',showcourse,name='showcourse'),
    path('editcourse/<int:id>/', editcourse, name='editcourse'),
    path('updatecourse/<int:id>/', updatecourse, name='updatecourse'),
    path('deletecourse/<int:id>/',deletecourse,name='deletecourse'),
    path('addstudent/',addstudent,name='addstudent'),
    path('logout/',logout,name='logout'),
] 