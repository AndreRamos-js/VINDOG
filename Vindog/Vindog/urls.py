from django.conf.urls import url
from racas.views import cadastrar_raca

urlpatterns = [
    url(r'^', cadastrar_raca, name='cadastrar_raca'),
    url(r'^cadastrar_raca/$', cadastrar_raca, name='cadastrar_raca'),
]
