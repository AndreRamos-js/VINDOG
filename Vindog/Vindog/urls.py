from django.conf.urls import url
from racas.views import CadastrarRacaCreateView, CadastrarCachorroCreateView, TemplateIndexView



urlpatterns = [
    url(r'^$', TemplateIndexView.as_view(), name='index'),
    url(r'^cadastrar_raca/$', CadastrarRacaCreateView.as_view(), name='cadastrar_raca'),
    url(r'^cadastrar_cachorro/$', CadastrarCachorroCreateView.as_view(), name='cadastrar_cachorro'),
]
