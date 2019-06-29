from .models import Reserva
from datetime import date
from . import numeracao

def atualiza():

    reservas = Reserva.objects.filter(data__lte=date.today()).filter(estado=numeracao.estadoReserva('aprovada'))

    for reserva in reservas:
        reserva.estado = numeracao.estadoReserva('finalizada')
        reserva.save()
