from django.views.generic import CreateView, TemplateView
from .forms import RacaForm
from .models import Raca
from .forms import CachorroForm
from .models import Cachorro



class TemplateIndexView(TemplateView):
    template_name = 'index.html'

class TemplateRelatorioView(TemplateView):
    template_name = 'relatorio.html'

class CadastrarRacaCreateView(CreateView):
    template_name = 'cadastrar_raca.html'
    form_class = RacaForm
    model = Raca
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['racas']=Raca.objects.all()
        return context
    
class CadastrarCachorroCreateView(CreateView):
    template_name = 'cadastrar_cachorro.html'
    form_class = CachorroForm
    model = Cachorro
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cachorros']=Cachorro.objects.all()
        return context
