from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app1.models import tweet
# Create your views here.
@login_required(login_url='loginpage')
def createview(request):
    if request.method=="POST":
        a=request.POST.get('post')
        u=str(request.user.username)
        obj=tweet(post=a,uname=u)
        obj.save()
    return render(request,'create.html')

def displayview(request):
    return render(request,'display.html')
def homeview(request):
    objs=tweet.objects.all()[::-1]
    if request.method=="POST":
        a=request.POST.get('sch')
        result=tweet.objects.filter(uname__icontains=a)
    return render(request,'home.html',{'resu':objs})
def loginview(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=="POST":
        a=request.POST.get('uname')
        b=request.POST.get('passw')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            login(request,result)
            print(a,b,result)
            return redirect('homepage')
        
        else:
            return redirect('loginpage')
    return render(request,'login.html')

@login_required(login_url='loginpage')
def profileview(request):
    if request.user.is_superuser:
        return redirect('/admin')
    else:
        return render(request,'profile.html')
def registerview(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        fn=request.POST.get('fname')
        c=request.POST.get('lname')
        d=request.POST.get('mail')
        p=request.POST.get('passw')
        pc=request.POST.get('cpass')
        print(un,fn,c,d,p,pc)
        if User.objects.filter(username=un).exists():
            return redirect('loginpage')
        if len(p)<8:
            return redirect('registerpage')
        if p!=pc:
            return redirect('registerpage')
        obj=User.objects.create_user(username=un,first_name=fn,last_name=c,email=d,password=p,)
        obj.save()
        return redirect('homepage')

    return render(request,'register.html')
def singleview(request):
    return render(request,'single.html')

def logoutview(request):
    logout(request)
    return redirect('loginpage')
