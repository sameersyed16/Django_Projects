from django.urls import path
from user import views
urlpatterns=[
    path('indianuser/<int:uid>',views.indianuser),
    path('ukuser/<int:uid>',views.ukuser),
    path('pakuser/<int:uid>',views.pakuser)
    
]

