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