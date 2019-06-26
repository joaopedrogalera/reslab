from django.db import models

class Usuario(models.Model):
    uid = models.CharField(max_length=20,primary_key=True)
    nome = models.CharField(max_length=50)
    email1 = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50)
    ra = models.CharField(max_length=10)
    categoria = models.CharField(max_length=1)
    cargo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.uid
