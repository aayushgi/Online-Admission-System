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
    path('showstudent/', showstudent, name='showstudent'),
    path('editcourse/<int:id>/', editcourse, name='editcourse'),
    path('updatecourse/<int:id>/', updatecourse, name='updatecourse'),
    path('deletecourse/<int:id>/',deletecourse,name='deletecourse'),
    path('addstudent/',addstudent,name='addstudent'),
    path('logout/',logout,name='logout'),
    path('course/', course, name='course'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('loginviahome/', loginviahome, name='loginviahome'),
    path('student_login/', student_login, name='student_login'),
    path('studentdash/',studentdash,name='studentdash'),
    path('apply1/', apply1, name='apply1'),
    path('apply2',apply2,name='apply2'),
] 