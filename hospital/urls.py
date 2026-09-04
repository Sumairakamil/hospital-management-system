from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients, name='patients'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointments/', views.appointments, name='appointments'),
    path('reports/', views.reports, name='reports'),

    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
]