from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import getNavbar
from . import numeracao
from .models import Usuario
from .models import Laboratorio
from .models import Horario
from .models import Reserva

def CadastroAulas(request):

    us = Usuario.objects.get(uid=request.session['uid'])

    if not us.categoria == numeracao.categoria('administrador'):
        return redirect('/dashboard')

    laboratorios = Laboratorio.objects.filter(adm__uid=us.uid)
    horarios = Horario.objects.all()

    context = {'navBarItens': getNavbar.navBar(request,'cadastroaulas'),
                'laboratorios': laboratorios,
                'horarios': horarios}

    return render(request,'cadastroaulas.html',context)

def CadastraAula(request):
    if not request.method == 'POST':
        return redirect('/cadastroaulas')

    us = Usuario.objects.get(uid=request.session['uid'])

    if not us.categoria == numeracao.categoria('administrador'):
        return redirect('/dashboard')

    laboratorio = Laboratorio.objects.get(sala=request.POST['lab'])

    aula = Reserva()

    aula.solicitante = us
    aula.diasemana = request.POST['dia']
    aula.lab = laboratorio
    aula.estado = numeracao.estadoReserva('aprovada')
    aula.tipo = numeracao.tipoReserva('aula')
    aula.save()

    horarios = request.POST.getlist('horario[]')

    for horario in horarios:
        horarioObj = Horario.objects.get(cod=horario)

        aula.horarios.add(horarioObj)

    context = {'navBarItens': getNavbar.navBar(request,'cadastroaulas')}
    return render(request,'cadastroaulas-confirmacao.html',context)
