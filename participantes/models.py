from django.db import models
from funcao.models import Funcao

class Participante(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=9)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    evangelico = models.BooleanField(default=False)
    igreja = models.CharField(max_length=255)
    funcao = models.ForeignKey(Funcao, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to='Participantes', blank=True, null=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
