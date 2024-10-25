from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request):
    bus={'bus':[{'no': 1,'route':'Ananthapur'},
                 {'no': 2,'route':'pamidi'},
                 {'no': 3,'route':'Tadipatri'},
                 {'no': 4,'route':'Dharmavaram'},
                 {'no': 5,'route':'tapovanam'}
                 ]
    }
    return render(request,'bus.html',bus)

def fun2(request):
    d2={'movie':[{'name':'End Game','director':'sameer','year':2020,'genre':'Action','IMDb':6},
                 {'name':'spaiderman','director':'Sam Raimi','year':2023,'genre':'spy','IMDb':8},
                 {'name':'Avatar','director':'James Cameron','year':2022,'genre':'Adventure','IMDb':9},
                 {'name':'interstellar','director':'Christopher Nolan','year':2014,'genre':'Sci-fi','IMDb':10}
                 ]
        }
    return render(request,'movie.html',d2)