from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva
from . import getNavbar
from . import numeracao

def getMinhasResevas(request):

    reservas = Reserva.objects.filter(solicitante=request.session['uid']).order_by('-data')

    context = {'navBarItens': getNavbar.navBar(request,'minhasreservas'),
                'reservas': reservas,
                }

    return render(request,'mostrareservas.html', context)
