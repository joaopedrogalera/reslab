from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import login
from . import dashboard
from . import minhasreservas
from . import cancelamento
from . import aprovacaoreservas
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

def loginError(request):
    return render(request,"loginError.html")

def showDashboard(request):
    if not request.session.get('exists',False):
        return redirect('/login')
    else:
        return dashboard.getDashBoard(request)

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
