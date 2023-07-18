from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.analyst_home, name= 'analyst'),
    path('viewPDF/', views.view_pdf),
 
]