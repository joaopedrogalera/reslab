from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import login
from . import getNavbar
from . import minhasreservas
from . import cancelamento
from . import aprovacaoreservas
from . import cadastroaulas
from . import novareserva
from .models import Usuario

def index(request):
    if not request.session.get('exists',False):
        return render(request,"login.html")
    else:
        return redirect('/dashboard')

@csrf_exempt
def doLogin(request):
    if not request.session.get('exists',False):
        return login.doLogin(request)
    else:
        return redirect('/dashboard')

def showDashboard(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        navBar = getNavbar.navBar(request,'dashboard')
        context = {'navBarItens': navBar}
        return render(request,'dashboard.html',context)

def showMinhasReservas(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return minhasreservas.getMinhasResevas(request)

def confirmCancelaReserva(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return cancelamento.confirmCancelaReserva(request)

def CancelaReserva(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return cancelamento.CancelaReserva(request)

def showReservasPendentes(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return aprovacaoreservas.showReservasPendentes(request)

def showDetalheReserva(request):
        if not request.session.get('exists',False):
            return redirect('/login')
        else:
            return aprovacaoreservas.showDetalheReserva(request)

def AprovaReserva(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return aprovacaoreservas.AprovaReserva(request)

def RecusaReserva(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return aprovacaoreservas.RecusaReserva(request)

def CadastroAulas(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return cadastroaulas.CadastroAulas(request)

@csrf_exempt
def CadastraAula(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return cadastroaulas.CadastraAula(request)

def NovaReservaSelSoft(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return novareserva.SelSoft(request)

@csrf_exempt
def NovaReservaBuscaSoftware(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return novareserva.BuscaSoftware(request)

@csrf_exempt
def NovaReservaMostraHorario(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return novareserva.MostraHorario(request)

@csrf_exempt
def NovaReservaSolicita(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return novareserva.Solicita(request)
