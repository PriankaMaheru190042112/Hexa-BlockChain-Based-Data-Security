from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.owner_home, name= 'owner'),
    path('uploadFiles/', views.upload_document),
    path('documentList/', views.document_list)
]