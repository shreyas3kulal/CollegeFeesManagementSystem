from django import forms
from django.forms.widgets import DateInput
from .models import Student,Staff
from django.forms import Textarea,DateInput


class Savestudent(forms.ModelForm):
    class Meta:
        model = Student
        fields =['AddmissionDate','Name','UniversitySeatNumber','Course','Semester','Email','PhoneNo','DateOfBirth','State','City','PinCode','Address']
        widgets = {
            'Address': Textarea(attrs={'cols': 60, 'rows': 5}),
            'DateOfBirth':DateInput(attrs={'type':'date'})
        }
class Savestaff(forms.ModelForm):
    class Meta:
        model = Staff
        fields =['Name','Salary','Email','PhoneNo','DateOfBirth','State','City','PinCode','Address']
        widgets = {
            'Address': Textarea(attrs={'cols': 60, 'rows': 5}),
            'DateOfBirth':DateInput(attrs={'type':'date'})
        }