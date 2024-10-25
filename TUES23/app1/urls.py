from django.urls import path
from app1 import views
urlpatterns=[
    path('bus',views.func1),
    path('mov',views.fun2)

]