from django.shortcuts import render
from django.http import HttpResponse
def text(request,name,age):
    return HttpResponse(f"hello {name} is {age} old")
def f1(request):
    return HttpResponse("Hello Everyone app1text")
def f2(request):
    return HttpResponse("Hello Everyone app1text11")

# Create your views here.
