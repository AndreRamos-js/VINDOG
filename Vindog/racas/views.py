from django.views.generic import CreateView, TemplateView
from .forms import RacaForm, CachorroForm
from .models import Raca, Cachorro
from .tasks import adicionar_raca, adicionar_cachorro
from django.http import HttpResponseRedirect



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

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        cores = form.cleaned_data['cores']
        pais = form.cleaned_data['pais']
        tamanho = form.cleaned_data['tamanho']
        descricao = form.cleaned_data['descricao']
        adicionar_raca.delay(nome, cores, pais, tamanho, descricao)
        return HttpResponseRedirect('/')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CadastrarCachorroCreateView(CreateView):
    template_name = 'cadastrar_cachorro.html'
    form_class = CachorroForm
    model = Cachorro
    success_url = '/'

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        peso = form.cleaned_data['peso']
        altura = form.cleaned_data['altura']
        sexo = form.cleaned_data['sexo']
        descricao = form.cleaned_data['descricao']
        personalidade = form.cleaned_data['personalidade']
        raca_id = form.cleaned_data['raca'].id
        adicionar_cachorro.delay(nome, peso, altura, sexo, descricao, personalidade, raca_id)
        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
