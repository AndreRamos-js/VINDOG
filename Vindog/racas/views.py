from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from .forms import RacaForm, CachorroForm
from .models import Raca, Cachorro



class TemplateIndexView(TemplateView):
    template_name = 'index.html'

class TemplateRelatorioView(TemplateView):
    template_name = 'relatorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['racas'] = Raca.objects.all()
        context['cachorros'] = Cachorro.objects.all()

        search_racas = self.request.GET.get('search_racas')
        search_cachorros = self.request.GET.get('search_cachorros')

        if search_racas:
            context['racas'] = Raca.objects.filter(nome__icontains=search_racas)

        if search_cachorros:
            context['cachorros'] = Cachorro.objects.filter(nome__icontains=search_cachorros)

        return context

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
