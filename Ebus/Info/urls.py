from django.urls import path
from Info import views
urlpatterns=[
    path('sam',views.businfo,name='home')
]