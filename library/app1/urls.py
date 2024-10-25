from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
enctype="multipart/form-data"
urlpatterns=[
    path('',views.homeview,name="homepage"),
    path('post',views.createview,name="authorpage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
