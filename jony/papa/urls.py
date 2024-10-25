from django.urls import path
from papa import views
urlpatterns=[
    path('<str:name>',views.jony)
]