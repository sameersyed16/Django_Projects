from django.urls import path
from today11 import views
urlpatterns=[
    path('<str:name>/<int:age>',views.text),
    path('hi1',views.f1),
    path('hi2',views.f2)
]