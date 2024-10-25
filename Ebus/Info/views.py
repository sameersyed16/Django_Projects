from django.shortcuts import render
from Info.models import businfo
# Create your views here.
def businfo(request):
    result=businfo.objects.all()
    return render(request)
