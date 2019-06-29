from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('doLogin',views.doLogin),
    path('loginError',views.loginError),
    path('dashboard',views.showDashboard),
    path('minhasreservas',views.showMinhasReservas),
    path('confirmacancelareserva',views.confirmCancelaReserva),
    path('cancelareserva',views.CancelaReserva)
]
