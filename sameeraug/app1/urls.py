from django.urls import path
from app1 import views
urlpatterns=[
    path('',views.homeview,name="homepage"),
    path('login',views.loginview,name="loginpage"),
    path('create',views.createview,name="createpage"),
    path('display',views.displayview,name="displaypage"),
    path('profile',views.profileview,name="profilepage"),
    path('register',views.registerview,name="registerpage"),
    path('single',views.singleview,name="singlepage"),
    path('logout',views.logoutview,name="logout"),

]