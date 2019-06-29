from django.db import models
from . import numeracao

class Usuario(models.Model):
    uid = models.CharField(max_length=20,primary_key=True)
    nome = models.CharField(max_length=50)
    email1 = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50,blank=True)
    ra = models.CharField(max_length=10)
    categoria = models.CharField(max_length=1)
    cargo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.uid

class Departamento(models.Model):
    sigla = models.CharField(max_length=5,primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.sigla

class Software(models.Model):
    nome = models.CharField(max_length=20)
    versao = models.CharField(max_length=50)

    class Meta:
        unique_together = ('nome','versao')

    def __str__(self):
        return self.nome + " " + self.versao

class Laboratorio(models.Model):
    sala = models.CharField(max_length=5,primary_key=True)
    nroComp = models.IntegerField()
    dpto = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    softwares = models.ManyToManyField(Software)
    adm = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.sala

class Horario(models.Model):
    cod = models.CharField(max_length=2)
    inicio = models.CharField(max_length=5)
    fim = models.CharField(max_length=5)

    def __str__(self):
        return self.cod

class Reserva(models.Model):
    solicitante = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    data = models.DateField(blank=True)
    diasemana = models.CharField(max_length=1,blank=True)
    lab = models.ForeignKey(Laboratorio,on_delete=models.CASCADE)
    horarios = models.ManyToManyField(Horario)
    estado = models.CharField(max_length=1)

    def Aprova(self):
        if self.estado == numeracao.estadoReserva('pendente'):
            self.estado = numeracao.estadoReserva('aprovada')
            self.save()

    def Recusa(self):
        if self.estado == numeracao.estadoReserva('pendente'):
            self.estado = numeracao.estadoReserva('recusada')
            self.save()

    def Cancela(self):
        if self.estado == numeracao.estadoReserva('pendente') or self.estado == numeracao.estadoReserva('aprovada'):
            self.estado = numeracao.estadoReserva('cancelada')
            self.save()
