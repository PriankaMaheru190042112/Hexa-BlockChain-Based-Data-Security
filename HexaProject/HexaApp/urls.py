from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home ,name='home'),
    path('about/',views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.form, name='form')

]