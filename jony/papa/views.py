from django.shortcuts import render
from django.http import HttpResponse
def jony(request,name):
    return HttpResponse(f"<p>{name} {name}<br>Yes papa?<br>Eating sugar?<br>No papa.<br>Telling lies?<br>No papa.<br>Open your mouth!<br>Ha ha ha!</p>")

# Create your views here.
