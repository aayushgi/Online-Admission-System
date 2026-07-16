from django.shortcuts import render,redirect
from .models import*
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'student/home.html')

def adminlogin(request):
    return render(request, 'admin/admin_login.html')

def loginsave(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=login.objects.filter(username=username,password=password).first()
        if user:
            if user.status=="Active":
                request.session['adminid']=username
                return redirect('dashboard')
        else:
            return redirect('adminlogin')
def dashboard(request):
    return render(request, 'admin/dashboard.html')


def admindash(request):
    return render(request, 'admin/adminlayout.html')


def addsession(request):
    if request.method=="POST":
        session_name=request.POST.get('session_name')
        create_at=datetime.now()
        sv=session.objects.filter(session_name=session_name).first()
        if sv:
            messages.warning(request, 'Session Already Exists')
            
        else:
            ab=session(session_name=session_name,create_at=create_at)
            ab.save()
            messages.success(request, 'Session Added Successfully')
        return redirect('addsession')
          
    return render(request, 'admin/addsession.html')

def deletesession(request,id):
    ab=session.objects.get(id=id)
    ab.delete()
    messages.success(request,'session Deleted Successfully')
    return redirect('showsession')

def editcourse(request, id):
    course = tbl_course.objects.get(id=id)
    sessions = session.objects.all()
    return render(request, 'admin/editcourse.html', {'course': course, 'sessions': sessions})


def updatecourse(request, id):
    course = tbl_course.objects.get(id=id)
    if request.method == "POST":
        course.session_name = request.POST.get('session_name')
        course.course_name = request.POST.get('course_name')
        course.duration = request.POST.get('duration')
        course.fees = request.POST.get('fees')
        course.save()
        messages.success(request, 'Course Updated Successfully')
        return redirect('showcourse')
    return render(request, 'admin/editcourse.html', {'course': course})

def deletecourse(request, id):
    course = tbl_course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course Deleted Successfully')
    return redirect('showcourse')


def showsession(request):
    ab=session.objects.all()
    return render(request, 'admin/showsession.html', {'ab':ab})

def addcourse(request):
    sessions=session.objects.all()
    if request.method=="POST":
        session_name=request.POST.get('session_name')
        course_name=request.POST.get('course_name')
        duration=request.POST.get('duration')
        fees=request.POST.get('fees')
        create_at=datetime.now()
        ab=tbl_course(session_name=session_name,course_name=course_name,duration=duration,fees=fees,create_at=create_at)
        ab.save()
        messages.success(request, 'Course Added Successfully')
        return redirect('addcourse')  
    return render(request, 'admin/addcourse.html',{'sessions':sessions})

def showcourse(request):
    ab=tbl_course.objects.all()
    return render(request, 'admin/showcourse.html', {'ab':ab})