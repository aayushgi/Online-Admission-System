from django.shortcuts import render,redirect
from .models import*
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
import hashlib


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
    total_student = tbl_student.objects.count()
    
    return render(request, 'admin/dashboard.html', {'total_session': total_session ,'total_course':total_course,'total_student':total_student})    

    


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

def showstudent(request):
    # Check admin login session
   

    ab = tbl_student.objects.all()
    return render(request, 'admin/showstudent.html', {'ab': ab})

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
            return redirect('student_login')
    return render(request, 'student/student_login.html')

def studentdash(request):
    email=request.session.get('studentid')
    student=tbl_student.objects.filter(emailaddress=email).first()
    context={
        'student':student
    }
    return render(request, 'student/studentdash.html',context)


def apply1(request):
    ab=tbl_course.objects.all()
    ad=session.objects.all()

    
    sid=request.session.get('studentid')
    data=tbl_student.objects.filter(emailaddress=sid).first()
    
    #dataget

    f_name=request.POST.get('f_name')
    m_name=request.POST.get('m_name')
    address=request.POST.get('address')
    addhar_no=request.POST.get('addhar_no')
    Session=request.POST.get('session')
    course=request.POST.get('cousre')

    #set data viya model
    data.f_name=f_name
    data.m_name=m_name
    data.addhar_no=addhar_no
    data.Session=Session
    data.course=course
    data.save()
    return redirect('apply2')
    context={
        'ab':ab,#this is for course
        'ad':ad,#this is for session
        'data':data,
        'student':data
    }
    sid=request.session.get('studentid')
    return render(request, 'student/apply1.html',context)
    

def apply2(request):
    sid=request.session.get('studentid')
    data=tbl_student.objects.get(emailaddress=sid)
    if request.method == 'POST':
        hs_percentage=request.POST.get('hs_percentage')
        hs_marksheet=request.FILES.get('hs_marksheet')
        inter_percentage=request.POST.get('inter_percentage')
        inter_marksheet=request.FILES.get('inter_marksheet')
        aadhar_pic=request.FILES.get('aadhar_pic')
        profile_pic=request.FILES.get('profile_pic')
        sign=request.FILES.get('sign')
    #set the data on model
        data.hs_percentage=hs_percentage
        data.hs_marksheet=hs_marksheet
        data.inter_percentage=inter_percentage
        data.inter_marksheet=inter_marksheet
        data.aadhar_pic=aadhar_pic
        data.profile_pic=profile_pic
        data.sign=sign
        data.application_status='DV'
        data.save()
        return redirect('studentdash')
    return render(request,'student/apply2.html')



def studentlogout(request):
    request.session.flush()
    return redirect('student_login')

def details_review(request, emailaddress):
    student = tbl_student.objects.get(emailaddress=emailaddress)

    return render(
        request,
        'admin/details_review.html',
        {
            'student': student
        }
    )

def reviewstudent(request):
    ab=tbl_student.objects.get(emailaddress=emailaddress)
    return render(request,'admin/showstudent.html',{'ab':ab})

def verify(request,emailaddress):
    student=tbl_student.objects.get(emailaddress=emailaddress)
    student.application_status="Approved"
    student.save()
    return redirect('details_review',emailaddress=emailaddress)



def get_login_student(request):
    sid = request.session.get('studentid')

    if sid:
        return tbl_student.objects.filter(emailaddress=sid).first()

    return None


def student_fees_payment(request):

    student = get_login_student(request)

    if not student:
        return redirect('student_login')

    return render(request, 'student/student_fees_payment.html', {
        'student': student
    })


def payu_payment(request):

    student = get_login_student(request)

    if not student:
        return redirect("student_login")

    if student.application_status != "Approved":
        messages.error(request, "Your documents are not approved yet.")
        return redirect("student_fees_payment")

    if student.fees_status == "Paid":
        messages.success(request, "Fees already paid.")
        return redirect("student_enrolled_course")

    # Get Course Details
    course = tbl_course.objects.filter(course_name=student.course).first()

    if course:
        amount = str(course.fees)
        productinfo = course.course_name

        # Student table me bhi update kar do
        student.fees = course.fees
        student.save()

    else:
        # Dummy values for testing
        amount = "1.00"
        productinfo = "Admission Fee"

    key = settings.PAYU_KEY
    salt = settings.PAYU_SALT
    payu_url = settings.PAYU_URL

    txnid = "TXN" + uuid.uuid4().hex[:10].upper()

    firstname = student.name
    email = student.emailaddress
    phone = str(student.contact_no)

    surl = request.build_absolute_uri("/payment_success/")
    furl = request.build_absolute_uri("/payment_failure/")

    hash_string = (
        f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|||||||||||{salt}"
    )

    hashh = hashlib.sha512(hash_string.encode()).hexdigest().lower()

    student.payment_id = txnid
    student.fees_status = "Pending"
    student.save()

    context = {
        "payu_url": payu_url,
        "key": key,
        "txnid": txnid,
        "amount": amount,
        "productinfo": productinfo,
        "firstname": firstname,
        "email": email,
        "phone": phone,
        "surl": surl,
        "furl": furl,
        "hash": hashh,
    }

    return render(request, "student/payu_redirect.html", context)

@csrf_exempt
def payment_success(request):

    txnid = request.POST.get("txnid")
    mihpayid = request.POST.get("mihpayid")
    status = request.POST.get("status")

    student = tbl_student.objects.filter(payment_id=txnid).first()

    if not student:
        return redirect("student_login")

    if status == "success":

        student.fees_status = "Paid"
        student.payment_date = datetime.now()

        if mihpayid:
            student.payment_id = mihpayid

        student.save()

        messages.success(request, "Payment Successful.")

        return redirect("student_enrolled_course")

    student.fees_status = "Failed"
    student.save()

    messages.error(request, "Payment Failed.")

    return redirect("student_fees_payment")


@csrf_exempt
def payment_failure(request):

    txnid = request.POST.get("txnid")

    student = tbl_student.objects.filter(payment_id=txnid).first()

    if student:
        student.fees_status = "Failed"
        student.save()

    messages.error(request, "Payment Failed.")

    return redirect("student_fees_payment")


def student_enrolled_course(request):

    student = get_login_student(request)

    if not student:
        return redirect("student_login")

    return render(request, "student/student_enrolled_course.html", {
        "student": student
    })