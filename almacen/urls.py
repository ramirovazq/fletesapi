from django.urls import path

from . import views

urlpatterns = [
    path('sincroniza/', views.sincroniza, name='sincroniza'),
    path('movimientos/', views.movimientos, name='movimientos'),
]