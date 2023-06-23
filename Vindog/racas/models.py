from django.db import models

class Raca(models.Model):
    TAMANHO_CHOICES = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    nome = models.CharField(max_length=100)
    cores = models.CharField(max_length=100 , null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    tamanho = models.CharField(max_length=1, choices=TAMANHO_CHOICES, default='P')
    descricao = models.TextField()

class Cachorro(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    descricao = models.TextField()
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
