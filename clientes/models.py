from django.db import models
from django.urls import reverse_lazy


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    fone = models.CharField(max_length=10)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('clientes:clientes_list')

