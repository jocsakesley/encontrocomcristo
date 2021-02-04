from django.db import models
from participantes.models import Participante

class Equipe(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    lider = models.ForeignKey(Participante, on_delete=models.DO_NOTHING, related_name="lider_equipe", null=True)
    membros = models.ManyToManyField(Participante, related_name="membros_equipe", null=True)

    def __str__(self):
        return self.nome