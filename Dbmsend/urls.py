"""Dbmsend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Newapp.views import *
from Newapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('FirstPage/',FirstPage),
    path('ViewStudentProfile/',ViewStudentProfile),
    path("AddName/",AddName),
    path("StudentNameRegister/",StudentNameRegister),
    path('HodLogin/',HodLogin),
    path('AdminLogin/',AdminLogin),
    path('StudenttLogin/',StudenttLogin),
    path('HodMain/',HodMain),
    path('AdminMain/',AdminMain),
    path('StudentMain/',StudentMain),
    path('AddStudent/',AddStudent),
    path('AddFees/',AddFees),
    path('AddStaff/',AddStaff),
    path('savedatafees/',savedatafees),
    path('ViewStaff/',ViewStaff),
    path('ViewStudent/',ViewStudent),
    path('ViewFees/',ViewFees),
    path('ViewStudentFees/',ViewStudentFees),
    path('PayFees/',PayFees),
    path('StudentLoginRegister/',StudentLoginRegister),
    path('StaffLoginRegister/',StaffLoginRegister),
    path('savestudentlogindata/',savestudentlogindata),
    path('savestafflogindata/',savestafflogindata),
    path('PaymentDone/',PaymentDone),
    path('PaymentMode/',PaymentMode),
    path('savepaidrecords/',savepaidrecords),
    path('ViewFeesRecord/',ViewFeesRecord),
    path('destroy/<int:id>',views.destroy),
    path('destruct/<str:id>',views.destruct),
    path('destructStaff/<str:id>',views.destructStaff),
    path('STUDENTLogin/',STUDENTLogin),
    path('STAFFLogin/',STAFFLogin),
    path('HODLogin/',HODLogin),
    path('feespendingstudentslist/',feespendingstudentslist),



]
