from django.urls import path
from app24 import views
urlpatterns=[
    path('home',views.home,name="homepage"),
    path('profile',views.profile,name="profilepage"),
    path('login',views.login,name="loginpage"),
    path('signup',views.signup,name="signuppage"),
    path('palin/<str:s>',views.palin,name="palinofnum")

]