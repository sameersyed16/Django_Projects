from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def loginview(request):
    if request.method=="POST":
        a=request.POST.get('s1')
        b=request.POST.get('p1')
        result=authenticate(request,username=a,password=b)
        print(a,b,type(result))
        login(request,result)
        messages.success(request,"mama logged")
        return render(request,'login.html',{'res':result})
    return render(request,'login.html')

def homeview(request):
    return render(request,'home.html')
def contactview(request):
    return render(request,'contact.html')
def dataview(request):
    return render(request,'data.html')
def userview(request):
    result=User.objects.all()
    return render(request,'user.html',{'res':result})
def userview1(request):
    Usern=request.POST.get('s1')
    Password=request.POST.get('p1')
    print(User,Password)
    
