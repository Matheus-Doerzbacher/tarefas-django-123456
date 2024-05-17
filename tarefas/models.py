from django.db import models
from django.utils import timezone


class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)
    realizada = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
