from django.urls import path
from racas.views import cadastrar_raca, relatorio_racas

urlpatterns = [
    path('cadastrar_raca/', cadastrar_raca, name='cadastrar_raca'),
    path('relatorio_racas/', relatorio_racas, name='relatorio_racas'),
]
