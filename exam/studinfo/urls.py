from django.urls import path
from studinfo import views
urlpatterns=[
    path('exam/<str:Rollno>',views.getinfo)

]