from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home ),
    path('OwnerLogin/', views.owner_login),
    path('OwnerRegister/', views.owner_register),
    
]