from django.urls import path
from kadapa import views
urlpatterns=[
    path('hi',views.bengal),
    path('hi2',views.kerala),
    path('hi3',views.gujarat)
    
]