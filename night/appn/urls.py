from django.urls import path
from appn import views
urlpatterns=[
    path('exam/<str:Rollno>',views.res,name="info"),
    path('sam',views.sameer,name="sameerpage")
]