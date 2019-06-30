
def navBar(texto):
    enum = {'dashboard': 0, 'novareserva': 1, 'minhasreservas': 2, 'aprovacaoreservas': 3, 'cadastroaulas': 4}

    return enum[texto]

def categoria(texto):
    enum = {'usuario': 'U', 'administrador': 'A'}

    return enum[texto]

def cargo(texto):
    enum = {'aluno': 'A', 'servidor': 'S'}

    return enum[texto]

def estadoReserva(texto):
    enum = {'pendente': 'P','aprovada': 'A','recusada': 'R', 'cancelada': 'C', 'finalizada': 'F'}

    return enum[texto]

def tipoReserva(texto):
    enum = {'reserva': 'R', 'aula': 'A'}

    return enum[texto]
