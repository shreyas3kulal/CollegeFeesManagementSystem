from django.shortcuts import render,redirect
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from Newapp.models import Student,Fees,PaymentRecord,Staff,user_type,StudentFeesReport
from django.views.decorators.csrf import csrf_exempt
from .forms import Savestudent,Savestaff
from django.contrib.auth.decorators import login_required
# Create your views here.
def FirstPage(request):
    return render(request,'mainpage.html')

@login_required
def HodMain(request):
    return render(request,'hodmain.html')
@login_required   
def AdminMain(request):
    return render(request,'adminmain.html')
@login_required
def StudentMain(request):
    obj=StudentFeesReport.objects.get(username=request.user)
    print(obj.Name)
    return render(request,'studentmain.html',{'Data':obj})
    

def HodLogin(request):
    return render(request,'hodlogin.html')
    
def AdminLogin(request):
    return render(request,'adminlogin.html')

def StudenttLogin(request):
     return render(request,'studentlogin.html')
@login_required
def StaffLoginRegister(request):
    return render(request,'staffloginregister.html')
@login_required
def StudentLoginRegister(request):
    return render(request,'studentloginregister.html')

@login_required
def AddStudent(request):
    if request.method=="POST":
        form=Savestudent(request.POST,request.FILES)
        form.save(commit=False).student=request.user 
        if form.is_valid():
            form.save()
            return render(request,'adminmain.html')
    else:
        form=Savestudent()
        return render(request,'addstudent.html',{'form':form } )


@login_required
def AddStaff(request):
    if request.method=="POST":
        form=Savestaff(request.POST)
        form.save(commit=False).staff=request.user
        if form.is_valid():
            form.save()
            return render(request,'hodmain.html')
    else:
        form=Savestaff()
        return render(request,'addstaff.html',{'form':form } )

@login_required
def AddFees(request):
    return render(request,'addfees.html')

@login_required
def PayFees(request):
    return render(request,'payfees.html')
@login_required
def PaymentMode(request):
    return render(request,'paymentmode.html')
@login_required
def PaymentDone(request):
    return render(request,'paymentdone.html')



@csrf_exempt
def savedatafees(request): 
    Feestype=request.POST.get('FT') 
    Feesamount=request.POST.get('FA')
    objs=Fees(FeesType=Feestype,FeesAmount=Feesamount)
    objs.save()
    return render(request,'adminmain.html')


@csrf_exempt
def savepaidrecords(request):
    Name=request.POST.get('name')
    Usn=request.POST.get('usn')
    Year=request.POST.get('Y') 
    Feestype=request.POST.get('FT') 
    objs=PaymentRecord(Name=Name,UniversitySeatNumber=Usn,Year=Year,FeesType=Feestype)
    usn=Usn
    feestype=Feestype
    if Feestype=='College Fees':
        post=Fees.objects.all()
        for x in post:
            if x.FeesType=='College Fees':
                objs.FeesAmount=x.FeesAmount
                val=x.FeesAmount
                objs.save()
    if Feestype=='Exam Fees':
        post=Fees.objects.all()
        for x in post:
            if x.FeesType=='Exam Fees':
                objs.FeesAmount=x.FeesAmount
                val=x.FeesAmount
                objs.save()
    if Feestype=='Hostel Fees':
        post=Fees.objects.all()
        print(post)
        for x in post:
            if x.FeesType=='Hostel Fees':
                objs.FeesAmount=x.FeesAmount
                val=x.FeesAmount
                objs.save()
    if Feestype=='Mess Fees':
        post=Fees.objects.all()
        print(post)
        for x in post:
            if x.FeesType=='Mess Fees':
                objs.FeesAmount=x.FeesAmount
                val=x.FeesAmount
                objs.save()
    if Feestype=='Bus Fees':
        post=Fees.objects.all()
        print(post)
        for x in post:
            if x.FeesType=='Bus Fees':
                objs.FeesAmount=x.FeesAmount
                val=x.FeesAmount
                objs.save()
    
    print(usn)
    print(feestype)
    try:
       ob=StudentFeesReport.objects.get(UniversitySeatNumber=usn)
    except Exception as e:
        
        messages.info(request,'Invalid USN')
        return redirect('/PayFees/')
        
    if feestype=='College Fees':
         ob.CollegeFees=val
         ob.save()
    elif feestype=='Exam Fees':
         ob.ExamFees=val
         ob.save()
    elif feestype=='Hostel Fees':
         ob.HostelFees=val
         ob.save()
    elif feestype=='Mess Fees':
         ob.MessFees=val
         ob.save()
    elif feestype=='Bus Fees':
         ob.BusFees=val
         ob.save()
  

    return redirect('/PaymentMode/')


@csrf_exempt
def savestudentlogindata(request):
    Username=request.POST.get('user')
    password=request.POST.get('p')  
    email=request.POST.get('e')
    try:
        objs=User.objects.create_user(username=Username,password=password,email=email)
    except Exception:
        messages.info(request,'Username Exists')
        return redirect('/StudentLoginRegister/')
    objs.save()
    user=auth.authenticate(username=Username,password=password)
    if user is not None:
        auth.login(request,user)
    usert = None
    if Username:
        usert = user_type(user=objs,is_student=True)
    usert.save()
    return redirect('/StudentNameRegister/')


@csrf_exempt
def savestafflogindata(request):
    Username=request.POST.get('username')
    password=request.POST.get('p')  
    email=request.POST.get('e')
    try:
        objs=User.objects.create_user(username=Username,password=password,email=email)
    except Exception:
        messages.info(request,'Username Exists')
        return redirect('/StaffLoginRegister/')
    objs.save()
    user=auth.authenticate(username=Username,password=password)
    if user is not None:
        auth.login(request,user)
    if Username:
        usert = user_type(user=objs,is_staff=True)
    usert.save()
    return redirect('/AddStaff/')

# Create your views here.
def ViewStudent(request):
    obj=Student.objects.all()
    return render(request,'viewstudent.html',{'Data':obj}) 


def ViewStaff(request):
    obj=Staff.objects.all()
    return render(request,'viewstaff.html',{'Data':obj})

@login_required
def ViewFees(request):
    obj=Fees.objects.all()
    return render(request,'viewfees.html',{'Data':obj}) 

@login_required
def ViewStudentFees(request):
    obj=Fees.objects.all()
    return render(request,'viewstudentfees.html',{'Data':obj}) 

@login_required
def ViewStudentProfile(request):
    obj=StudentFeesReport.objects.get(username=request.user)
    print(obj.Name)
    return render(request,'MyProfile.html',{'Data':obj})

@login_required
def ViewFeesRecord(request):
    obj=PaymentRecord.objects.all()
    return render(request,'studentmain.html',{'Data':obj})


def destroy(request,id):
    fees=Fees.objects.get(pk=id)
    fees.delete()
    return redirect('/ViewFees/')


def destruct(request,id):
    student=User.objects.get(username=id)
    student.delete()
    return redirect('/ViewStudent/')

def destructStaff(request,id):
    staff=User.objects.get(username=id)
    staff.delete()
    try:
        staff=StudentFeesReport.object.get(username=id)
        staff.delete()
    except Exception as e:
        pass
    return redirect('/ViewStaff/')

@csrf_exempt
def STUDENTLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            try:
                type_obj = user_type.objects.get(user=user)
            except Exception:
                return redirect('/StudenttLogin/')
                messages.info(request,'Invalid credentials')
            if user.is_authenticated and type_obj.is_student:
                #return redirect("/StudentMain/")
                return render(request,'studentmain.html',{'Data':user}) 
            else:
                messages.info(request,'Invalid credentials')
                return redirect('/StudenttLogin/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/StudenttLogin/')
    else:
        return render(request,'studentlogin.html')


@csrf_exempt
def STAFFLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('Shreyas')
            try:
                type_obj = user_type.objects.get(user=user)
            except Exception:
                messages.info(request,'Invalid credentials')
                return redirect('/AdminLogin/')
            if user.is_authenticated and type_obj.is_staff:
                return redirect("/AdminMain/")
            else:
                messages.info(request,'Invalid credentials')
                return redirect("/AdminLogin/")       
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/AdminLogin/')
    else:
        return render(request,'adminlogin.html')

@csrf_exempt
def HODLogin(request):
    if request.method=='POST':
        Username=request.POST['user']
        Password=request.POST['p']
        user=auth.authenticate(username=Username,password=Password)
        if user is not None:
            auth.login(request,user)
            try:
                type_obj = User.objects.get(username=user)
            except Exception:
                messages.info(request,'Invalid credentials')
                return redirect('/HodLogin/')
            if user.is_authenticated and type_obj.is_superuser:
               # return redirect("/HodMain/")
                return render(request,'hodmain.html',{'Data':user}) 
            else:
                messages.info(request,'Invalid credentials')
                return redirect('/HodLogin/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/HodLogin/')
    else:
        return render(request,'hodlogin.html')





def AddName(request):
    Name=request.POST.get('name') 
    Usn=request.POST.get('usn') 
    objs=StudentFeesReport(Name=Name,UniversitySeatNumber=Usn,username=request.user)
    objs.save()

    return redirect('/AddStudent/')
def StudentNameRegister(request):
    return render(request,'studentnameregister.html')

def feespendingstudentslist(request):
    cursor=connection.cursor()
    cursor.execute("call feespendingstudentslistSP()")
    results=cursor.fetchall()
    return render(request,'index.html',{'StudentFeesReport': results})



