from .models import Usuario
from . import numeracao

def navBar(request, pagAtual):
    us = Usuario.objects.get(uid=request.session['uid'])

    if us.categoria == numeracao.categoria('usuario'):
        navbar = [ ['dashboard',"Dashboard",''],
                    ['novareserva',"Nova Reserva",''],
                    ['minhasreservas',"Minhas Reservas",''],
                    ['logout',"Sair"]
                    ]
    else:
        navbar = [ ['dashboard',"Dashboard",''],
                    ['novareserva',"Nova Reserva",''],
                    ['minhasreservas',"Minhas Reservas",''],
                    ['aprovacaoreservas',"Aprovação de reservas",''],
                    ['cadastroaulas',"Cadastro de aulas",''],
                    ['logout',"Sair"]
                    ]


    navbar[numeracao.navBar(pagAtual)][2] = 'active'

    return navbar
