from django.shortcuts import render,redirect
from .models import*
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
    total_session = session.objects.count()
    total_course = tbl_course.objects.count()
    
    return render(request, 'admin/dashboard.html', {'total_session': total_session ,'total_course':total_course})    

    


#def admindash(request):
    total_session = session.objects.count()

    return render(request, 'admin/dashboard.html',{'total_session': total_session})

def course(request):
    return render(request, 'student/course.html')

def about(request):
    return render(request, 'student/about.html')

def contact(request):
    return render(request, 'student/contact.html')

def loginviahome(request):
    return render(request, 'student/login.html')


def addsession(request):
    
    # Check admin login session
    if 'adminid' not in request.session:
        return redirect('adminlogin')

    sessions = session.objects.all()
    
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
    messages.info(request,'session Deleted Successfully')
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
        messages.info(request, 'Course Updated Successfully')
        return redirect('showcourse')
    return render(request, 'admin/editcourse.html', {'course': course})

def deletecourse(request, id):
    course = tbl_course.objects.get(id=id)
    course.delete()
    messages.info(request, 'Course Deleted Successfully')
    return redirect('showcourse')


def showsession(request):
    ab=session.objects.all()
    return render(request, 'admin/showsession.html', {'ab':ab})

def addcourse(request):

    # Check admin login session
    if 'adminid' not in request.session:
        return redirect('adminlogin')

    sessions = session.objects.all()

    if request.method == "POST":
        session_name = request.POST.get('session_name')
        course_name = request.POST.get('course_name')
        duration = request.POST.get('duration')
        fees = request.POST.get('fees')
        create_at = datetime.now()

        ab = tbl_course(
            session_name=session_name,
            course_name=course_name,
            duration=duration,
            fees=fees,
            create_at=create_at
        )
        ab.save()

        messages.success(request, 'Course Added Successfully')
        return redirect('addcourse')

    return render(
        request,
        'admin/addcourse.html',
        {'sessions': sessions}
    )

def showcourse(request):
    ab=tbl_course.objects.all()
    return render(request, 'admin/showcourse.html', {'ab':ab})

def logout(request):
    request.session.flush()
    return redirect('adminlogin')
def addstudent(request):
    if request.method == "POST":

        name = request.POST.get('name')
        emailaddress = request.POST.get('emailaddress')
        password = request.POST.get('password')

        tbl_student.objects.create(
            name=name,
            emailaddress=emailaddress,
            password=password,
            contact_no=request.POST.get('contact_no'),
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob'),
        )

        message = f"""
Dear {name},

🎉 Congratulations!

Your registration has been completed successfully on the Biotech Park Admission Portal.

You can now log in using the credentials below:

---------------------------------------
User ID / Email : {emailaddress}
Password        : {password}
---------------------------------------

Next Steps:
1. Login to the Admission Portal.
2. Complete your Basic Information.
3. Upload all required documents.
4. Wait for document verification by the Admin.
5. After verification, pay your admission fee.
6. Once the payment is successful, your course will be allotted.

Please keep this email safe for future login and admission-related communication.

Regards,
Biotech Park Admission Team
"""
        

        send_mail(
            subject="Registration Successful",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[emailaddress],
             fail_silently=False
        )

        messages.success(request, "Student Added Successfully")
        return redirect('addstudent')

    return render(request, 'admin/adduser.html')



    #--------------------------------------------------------------------student shows-------------------------------------------------------------------------------
    
    
    
def student_login(request):
    if request.method == "POST":
        emailaddress = request.POST.get('emailaddress')
        password = request.POST.get('password')
        user = tbl_student.objects.filter(emailaddress=emailaddress, password=password).first()
        print(user)
        if user:
            request.session['studentid'] = emailaddress
            return redirect('studentdash')
        
        else:
            return redirect('studentlogin')
    return render(request, 'student/student_login.html')

def studentdash(request):
    return render(request, 'student/studentdash.html')


def apply1(request):
    ab=tbl_course.objects.all()
    ad=session.objects.all()
    context={
        'ab':ab,#this is for course
        'ad':ad #this is for session
    }
    return render(request, 'student/apply1.html', context)
    