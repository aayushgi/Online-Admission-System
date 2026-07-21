from django.db import models

# Create your models here.
class login(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=16)
    status=models.CharField(max_length=20)

class session(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    session_name=models.CharField(max_length=20)
    create_at=models.TimeField()


class tbl_course(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    session_name=models.CharField(max_length=20)
    course_name=models.CharField(max_length=200)
    duration=models.CharField(max_length=20)
    fees=models.IntegerField()
    create_at=models.TimeField() 


class tbl_student(models.Model):
    sid=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=225,null=True)
    emailaddress=models.EmailField(max_length=225,null=True)
    password=models.CharField(max_length=16,null=True)
    contact_no=models.IntegerField(null=True)
    gender=models.CharField(max_length=2,null=True)
    dob=models.DateField(null=True,blank=True)
    f_name=models.CharField(max_length=255,null=True)
    m_name=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=500,null=True)
    aadhar_no=models.IntegerField(blank=True,null=True)
    aadhar_pic=models.FileField(upload_to='student_documents',null=True)
    Session=models.CharField(max_length=50,null=True)
    course=models.CharField(max_length=500,null=True)
    course_duration=models.CharField(max_length=50,null=True)
    hs_percentage=models.CharField(max_length=20,null=True)
    hs_marksheet=models.FileField(upload_to='student_documents',null=True)
    inter_percentage=models.CharField(max_length=20,null=True)
    inter_marksheet=models.FileField(upload_to='student_documents',null=True)
    profile_pic=models.FileField(upload_to='student_documents',null=True)
    sign=models.FileField(upload_to='student_documents',null=True)
    application_status=models.CharField(max_length=20,null=True)
    fees=models.IntegerField(null=True)
    fees_status=models.CharField(max_length=20,null=True)