from django.urls import path
from icecream import views
urlpatterns=[
    path('sam/<int:no>/<int:cost>',views.func1,name="sameer"),
    path('sam1',views.func2)
]