from django.shortcuts import render, redirect
from .models import Software
from .models import Laboratorio
from .models import Horario
from .models import Reserva
from .models import Usuario
from . import getNavbar
from . import numeracao
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime

def SelSoft(request):

    softwares = Software.objects.all()

    context = {'navBarItens': getNavbar.navBar(request,'novareserva'),
                'softwares': softwares}

    return render(request,'novareserva-selectsoftware.html',context)

def BuscaSoftware(request):

    laboratorios = Laboratorio.objects.all()

    if request.method == 'POST':
        softwares = request.POST.getlist('software[]')

        for software in softwares:
            laboratorios = laboratorios.filter(softwares__id=software)

    if not laboratorios:
        context = {'navBarItens': getNavbar.navBar(request,'novareserva')}
        return render(request,'novareserva-selectsoftware-error.html',context)

    context = {'navBarItens': getNavbar.navBar(request,'novareserva'),
                'laboratorios': laboratorios}

    return render(request,'novareserva-listalabs.html',context)

def MostraHorario(request):

    if not request.method == 'POST' or request.POST.get('data','') == '' or request.POST.get('lab','') == '':
        return HttpResponse('<script type="text/javascript">window.history.go(-1)</script>')

    horarios = Horario.objects.all()

    listaHorariosUtilizados = []
    disableHorarios = []

    for horario in horarios:
        listaHorariosUtilizados.append('Livre')
        disableHorarios.append('')

    laboratorio = Laboratorio.objects.get(sala=request.POST['lab'])
    reservasDia = Reserva.objects.filter((Q(data=datetime.strptime(request.POST['data'],"%Y-%m-%d")) | Q(diasemana=datetime.strptime(request.POST['data'],"%Y-%m-%d").weekday())) & Q(lab=laboratorio) & (Q(estado=numeracao.estadoReserva('aprovada')) | Q(estado=numeracao.estadoReserva('pendente'))))

    for reservaDia in reservasDia:
        for horario in reservaDia.horarios.all():
            listaHorariosUtilizados[horario.id-1] = 'Ocupado'
            disableHorarios[horario.id-1] = 'disabled'

    context = {'navBarItens': getNavbar.navBar(request,'novareserva'),
                'horarios': horarios,
                'listaHorariosUtilizados':listaHorariosUtilizados,
                'disableHorarios':disableHorarios,
                'data': datetime.strptime(request.POST['data'],"%Y-%m-%d"),
                'lab': laboratorio
    }

    return render(request,'novareserva-horarios.html',context)

def Solicita(request):
    if not request.method == 'POST' or request.POST.get('data','') == '' or request.POST.get('lab','') == '' or request.POST.getlist('horario[]') == []:
        return HttpResponse('<script type="text/javascript">window.history.go(-1)</script>')

    us = Usuario.objects.get(uid=request.session['uid'])
    laboratorio = Laboratorio.objects.get(sala=request.POST['lab'])

    reserva = Reserva()

    reserva.solicitante = us
    reserva.data = datetime.strptime(request.POST['data'],"%Y-%m-%d")
    reserva.lab = laboratorio
    reserva.estado = numeracao.estadoReserva('pendente')
    reserva.tipo = numeracao.tipoReserva('reserva')
    reserva.save()

    horarios = request.POST.getlist('horario[]')

    for horario in horarios:
        horarioObj = Horario.objects.get(cod=horario)

        reserva.horarios.add(horarioObj)

    context = {'navBarItens': getNavbar.navBar(request,'novareserva')}
    return render(request,'novareserva-confirm.html', context)
