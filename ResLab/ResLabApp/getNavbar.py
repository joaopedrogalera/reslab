from .models import Usuario

def navBar(request, pagAtual):
    us = Usuario.objects.get(uid=request.session['uid'])

    if us.categoria == '0':
        navbar = [ ['dashboard',"Dashboard",''],
                    ['novareserva',"Nova Reserva",''],
                    ['minhasreservas',"Minhas Reservas",''],
                    ]
    else:
        navbar = [ ['dashboard',"Dashboard",''],
                    ['novareserva',"Nova Reserva",''],
                    ['minhasreservas',"Minhas Reservas",''],
                    ['aprovacaoreservas',"Aprovação de reservas",''],
                    ['cadastroaulas',"Cadastro de aulas",'']
                    ]

    enum = {'dashboard': 0, 'novareserva': 1, 'minhasreservas': 2, 'aprovacaoreservas': 3, 'cadastroaulas': 4}

    navbar[enum[pagAtual]][2] = 'active'
    
    return navbar
