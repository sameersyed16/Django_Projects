from django.shortcuts import render
from room.models import menu
# Create your views here.
def memu(request):
    result=menu.objects.all()
    return render(request,'index.html',bus:res)

