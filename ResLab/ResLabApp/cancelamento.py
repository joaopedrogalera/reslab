from .models import Reserva
from django.shortcuts import render, redirect
from django.http import HttpResponse

def confirmCancelaReserva(request):

    reserva = Reserva.objects.get(id=request.GET['id'])

    if not reserva.solicitante.uid == request.session['uid']:
        return redirect('/minhasreservas')

    context = {'reserva': reserva}
    return render(request,'minhasreservas-cancela.html',context)


def CancelaReserva(request):

    reserva = Reserva.objects.get(id=request.GET['id'])

    if not reserva.solicitante.uid == request.session['uid']:
        return redirect('/minhasreservas')

    reserva.Cancela()

    return redirect('/minhasreservas')
