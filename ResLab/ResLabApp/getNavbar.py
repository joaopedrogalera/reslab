from .models import Usuario

def navBar(request):
    us = Usuario.objects.get(uid=request.session['uid'])

    if us.categoria == '0':
        navbar = {'dashboard': ["Dashboard",''],
                    'novareserva': ["Nova Reserva",''],
                    'minhasreservas': ["Minhas Reservas",''],
                    }
    else:
        navbar = {'dashboard': ["Dashboard",''],
                    'novareserva': ["Nova Reserva",''],
                    'minhasreservas': ["Minhas Reservas",''],
                    'aprovacaoreservas': ["Aprovação de reservas",''],
                    'cadastroaulas': ["Cadastro de aulas",'']
                    }

    return navbar
