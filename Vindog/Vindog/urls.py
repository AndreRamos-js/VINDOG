from django.conf.urls import url
from racas.views import CadastrarRacaCreateView, CadastrarCachorroCreateView,\
TemplateIndexView, TemplateRelatorioRacaView, TemplateRelatorioCachorroView,\
EditarRacaView, EditarCachorroView, ExcluirRacaView, ExcluirCachorroView



urlpatterns = [
    url(r'^$', TemplateIndexView.as_view(), name='index'),
    url(r'^cadastrar_raca/$', CadastrarRacaCreateView.as_view(), name='cadastrar_raca'),
    url(r'^cadastrar_cachorro/$', CadastrarCachorroCreateView.as_view(), name='cadastrar_cachorro'),
    url(r'^relatorio_raca/$', TemplateRelatorioRacaView.as_view(), name='relatorio_raca'),
    url(r'^relatorio_cachorro/$', TemplateRelatorioCachorroView.as_view(), name='relatorio_cachorro'),
    url(r'^editar_raca/$', EditarRacaView.as_view(), name='editar_raca'),
    url(r'^editar_cachorro/$', EditarCachorroView.as_view(), name='editar_cachorro'),
    url(r'^excluir_raca/$', ExcluirRacaView.as_view(), name='excluir_raca'),
    url(r'^excluir_cachorro/$', ExcluirCachorroView.as_view(), name='excluir_cachorro'),
]
