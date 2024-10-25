from django.shortcuts import render
from icecream.models import menu
# Create your views here.
def func1(request,no,cost):
    obj=menu.objects.get(id=no)
    obj.price=cost
    obj.save()
    return render(request,"index.html",{'result':obj})
def func2(request):
    res=menu.objects.all()
    if request.method=='POST':
        sno=request.POST.get('sno')
        Brand_new=request.POST.get('Brand')
        result=menu.objects.get(id=sno)
        result.brand=Brand_new
        result.save()
        res=menu.objects.all()
        return render(request,"index2.html")
    return render(request,"index2.html")