from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('doLogin',views.doLogin),
    path('loginError',views.loginError),
    path('dashboard',views.showDashboard)
]
