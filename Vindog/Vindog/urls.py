from django.conf.urls import url
from racas.views import CadastrarRacaView

urlpatterns = [
    url(r'^', CadastrarRacaView.as_view(), name='cadastrar_raca'),
    url(r'^cadastrar_raca/$', CadastrarRacaView.as_view(), name='cadastrar_raca'),
]
