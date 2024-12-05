from django.db import models
from django.contrib.auth.models import User

class Treino(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Exercicio(models.Model):
    treino = models.ForeignKey(Treino, related_name='exercicios', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    repeticoes = models.PositiveIntegerField()
    tempo_descanso = models.DurationField(help_text='Tempo de descanso entre repetições (hh:mm:ss)')
    peso = models.DecimalField(max_digits=5, decimal_places=2, help_text='Peso em kg')
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
