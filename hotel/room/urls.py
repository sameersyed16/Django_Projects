from django.urls import path
from room import views
urlpatterns=[
    path('sam',views.memu,name='home')
]