from .models import Reserva
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import getNavbar

def confirmCancelaReserva(request):

    reserva = Reserva.objects.get(id=request.GET['id'])

    if not reserva.solicitante.uid == request.session['uid']:
        return redirect('/minhasreservas')

    context = {'reserva': reserva,
                'navBarItens': getNavbar.navBar(request,'minhasreservas')}
    return render(request,'minhasreservas-cancela.html',context)


def CancelaReserva(request):

    reserva = Reserva.objects.get(id=request.GET['id'])

    if not reserva.solicitante.uid == request.session['uid']:
        return redirect('/minhasreservas')

    reserva.Cancela()

    return redirect('/minhasreservas')
