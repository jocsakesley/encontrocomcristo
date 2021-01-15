from django.db import models

class Funcao(models.Model):
    funcao = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.funcao
