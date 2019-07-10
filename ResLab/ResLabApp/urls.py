from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('doLogin',views.doLogin),
    path('dashboard',views.showDashboard),
    path('minhasreservas',views.showMinhasReservas),
    path('confirmacancelareserva',views.confirmCancelaReserva),
    path('cancelareserva',views.CancelaReserva),
    path('aprovacaoreservas',views.showReservasPendentes),
    path('detalhereserva',views.showDetalheReserva),
    path('aprovareserva',views.AprovaReserva),
    path('recusareserva',views.RecusaReserva),
    path('cadastroaulas',views.CadastroAulas),
    path('cadastraaula',views.CadastraAula),
    path('novareserva',views.NovaReservaSelSoft),
    path('novareserva.buscasoftwares',views.NovaReservaBuscaSoftware),
    path('novareserva.mostrahorario',views.NovaReservaMostraHorario),
    path('novareserva.solicita',views.NovaReservaSolicita),
    path('logout',views.Logout),
    path('login',views.LoginPage)
]
