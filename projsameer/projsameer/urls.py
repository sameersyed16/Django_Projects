cd.\youtube\
class base views
functions views
in app we have to add urls.py
write this in views.py from django.http import HttpResponse
def fun_name(request):
return HttpResponse("messages any")
[triggers will write  add in urls.py of created app]
1.from django.urls import path
2.from created app name like shorts import views
urlspatterns=[(two parameters is use)
path('hi',views.wish), (each function has one trigger)
(urls means to provide path)
to create highway we use project urls.py
from django.url import path,include
path('app1/',include('appname.url'),
(to create apps python manage startapp app name)
to display message app1/abc/hi