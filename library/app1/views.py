from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from app1.models import insta
# Create your views here.
def createview(request):
    if request.method=="POST":
        a=request.POST.get('caption')
        b=request.FILES.get('img')
        u=request.user
        print(a,b,u)
        obj=insta(person=u,caption=a,pic=b)
        obj.save()
    return render(request,'create.html')
def homeview(request):
    objs=insta.objects.all()
    return render(request,'home.html',{'res':objs})
