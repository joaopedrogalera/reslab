from django.shortcuts import render, redirect
from .models import Usuario
from .models import Reserva
from django.http import HttpResponse
from . import numeracao
from . import getNavbar

def showReservasPendentes(request):
    us = Usuario.objects.get(uid=request.session['uid'])

    if not us.categoria == numeracao.categoria('administrador'):
        return redirect('/dashboard')

    reservas = Reserva.objects.filter(lab__adm__uid=us.uid).filter(estado=numeracao.estadoReserva('pendente')).order_by('-data')

    context = {'reservas': reservas,
                'navBarItens': getNavbar.navBar(request,'aprovacaoreservas')}

    return render(request,'aprovacao-mostrareservas.html',context)

def showDetalheReserva(request):
    us = Usuario.objects.get(uid=request.session['uid'])

    if not us.categoria == numeracao.categoria('administrador'):
        return redirect('/dashboard')

    reserva = Reserva.objects.get(id=request.GET['id'])

    if not reserva.lab.adm.uid == us.uid:
        return redirect('/aprovacaoreservas')

    context = {'reserva': reserva,
                'navBarItens': getNavbar.navBar(request,'aprovacaoreservas')}

    return render(request,'aprovacao-detalhereserva.html',context)

def AprovaReserva(request):
    us = Usuario.objects.get(uid=request.session['uid'])

    if not us.categoria == numeracao.categoria('administrador'):
        return redirect('/dashboard')

    reserva = Reserva.objects.get(id=request.GET['id'])

    if not reserva.lab.adm.uid == us.uid:
        return redirect('/aprovacaoreservas')

    reserva.Aprova()

    return redirect('/aprovacaoreservas')

def RecusaReserva(request):
    us = Usuario.objects.get(uid=request.session['uid'])

    if not us.categoria == numeracao.categoria('administrador'):
        return redirect('/dashboard')

    reserva = Reserva.objects.get(id=request.GET['id'])

    if not reserva.lab.adm.uid == us.uid:
        return redirect('/aprovacaoreservas')

    reserva.Recusa()

    return redirect('/aprovacaoreservas')
