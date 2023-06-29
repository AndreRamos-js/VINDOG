from django.conf.urls import url
from racas.views import CadastrarRacaCreateView, CadastrarCachorroCreateView,\
TemplateIndexView, TemplateRelatorioRacaView, TemplateRelatorioCachorroView



urlpatterns = [
    url(r'^$', TemplateIndexView.as_view(), name='index'),
    url(r'^cadastrar_raca/$', CadastrarRacaCreateView.as_view(), name='cadastrar_raca'),
    url(r'^cadastrar_cachorro/$', CadastrarCachorroCreateView.as_view(), name='cadastrar_cachorro'),
    url(r'^relatorio_raca/$', TemplateRelatorioRacaView.as_view(), name='relatorio_raca'),
    url(r'^relatorio_cachorro/$', TemplateRelatorioCachorroView.as_view(), name='relatorio_cachorro'),
]
