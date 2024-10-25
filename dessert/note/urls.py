from django.urls import path
from note import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
]
