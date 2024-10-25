from django.urls import path
from data import views 


urlpatterns=[
    path('',views.homeview,name="homepage"),
    path('login',views.loginview,name="loginpage"),
    path('profile',views.profile,name="profilepage"),
    path('logout',views.logoutV,name="logoutpage"),

]