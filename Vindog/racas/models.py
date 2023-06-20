from django.db import models



class Raca(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
