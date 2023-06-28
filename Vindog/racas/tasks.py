from celery import shared_task
from .models import Raca, Cachorro



@shared_task()
def adicionar_raca(nome, cores, pais, tamanho, descricao):
    raca = Raca(nome=nome, cores=cores, pais=pais, tamanho=tamanho, descricao=descricao)
    raca.save()
    return f"Raça {nome} adicionada com sucesso!"
    
@shared_task()
def adicionar_cachorro(nome, peso, altura, sexo, descricao, personalidade, raca_id):
    raca = Raca.objects.get(id=raca_id)
    cachorro = Cachorro(nome=nome, peso=peso, altura=altura, sexo=sexo, descricao=descricao, personalidade=personalidade, raca=raca)
    cachorro.save()
    return f"Cachorro {nome} adicionado com sucesso!"
