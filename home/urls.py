from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home,name='Home'),
    path('doctors/', views.Doctors,name='doctors'),
    path('Appointment/', views.Appointment,name='Appointment'),
    path('departments/', views.Department,name='departments'),
    path('Confirmation/',views.Confirmation,name='Confirmation')  
    ]