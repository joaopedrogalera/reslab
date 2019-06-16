from django.db import models

class usuario(models.Model):
    uid = models.CharField(max_length=20,primary_key=True)
    nome = models.CharField(max_length=50)
    email1 = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50)
    ra = models.IntegerField()
    categoria = models.CharField(max_length=1)
