
from django.db import models
from django.contrib.auth.models import User
from django.forms import widgets
from django.shortcuts import render,redirect
from django.utils import timezone
from django import forms
from django.db.models.signals import post_save



# Create your models here.



class Student(models.Model):
    AddmissionDate=models.CharField(max_length=30)
    Name=models.CharField(max_length=30)
    UniversitySeatNumber=models.CharField(max_length=30)
    Course=models.CharField(max_length=30)
    Semester=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    PhoneNo=models.CharField(max_length=30)
    DateOfBirth=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    PinCode=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    student =models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='Student'
    
class Fees(models.Model):
    FeesType=models.CharField(max_length=30)
    FeesAmount=models.CharField(max_length=30)
    
    class Meta:
        db_table='Fees'

class PaymentRecord(models.Model):
    Name=models.CharField(max_length=30)
    UniversitySeatNumber=models.CharField(max_length=30)
    Year=models.CharField(max_length=30)
    FeesType=models.CharField(max_length=30)
    FeesAmount=models.IntegerField(default=0)
    Date=models.DateField(default='2021-01-01')
    Time=models.TimeField(default='00:00:00')

    class Meta:
        db_table='PaymentRecord'

class StudentFeesReport(models.Model):
    Name=models.CharField(max_length=30)
    UniversitySeatNumber=models.CharField(max_length=30)
    CollegeFees=models.IntegerField(default=0)
    ExamFees=models.IntegerField(default=0)
    HostelFees=models.IntegerField(default=0)
    MessFees=models.IntegerField(default=0)
    BusFees=models.IntegerField(default=0)
    username =models.ForeignKey(User, on_delete=models.CASCADE)




    class Meta:
        db_table='StudentFeesReport'

class Staff(models.Model):
    
    Name=models.CharField(max_length=30)
    Salary=models.IntegerField(max_length=30)
    Email=models.EmailField(max_length=30)
    PhoneNo=models.IntegerField()
    DateOfBirth=models.DateField(blank=False)
    State=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    PinCode=models.IntegerField(max_length=6)
    Address=models.CharField(max_length=80)
    staff =models.ForeignKey(User, on_delete=models.CASCADE)

    
    class Meta:
        db_table='Staff'



class user_type(models.Model):
    is_staff= models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    class Meta:
        db_table='user_type'

def paymentdateandtime(sender,instance,created,**kwargs):
    if created:
        instance.Date=timezone.now()
        instance.Time=timezone.localtime()
        instance.save()
        
            
            
    else:
        print("errror")
post_save.connect(paymentdateandtime,sender=PaymentRecord)