from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home ),
    path('OwnerLogin/', views.owner_login),
    path('OwnerRegister/', views.owner_register),
    path('RegulatorLogin/', views.regulator_login),
    path('RegulatorRegister/', views.regulator_register),
    path('AnalystLogin/', views.analyst_login),
    path('AnalystRegister/', views.analyst_register),
    

]