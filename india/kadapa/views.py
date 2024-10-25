from django.shortcuts import render
from django.http import HttpResponse
def bengal(request):
    return HttpResponse("1.Durga Puja,2.Dol Purnima,3.Ratha Yatra,4.Kali Puja")
def gujarat(request):
    return HttpResponse("1.Navratri Puja,2.Rann Utsav,3.Shamlaji Melo")
def kerala(request):
    return HttpResponse("1.Onam,2.Vishuv,3.Thrissur Pooram")
    
# Create your views here.
