from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import getNavbar
from . import numeracao
from .models import Usuario
from .models import Laboratorio
from .models import Horario

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
