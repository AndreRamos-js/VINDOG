from django.views.generic import CreateView, TemplateView, View
from .forms import RacaForm, CachorroForm
from .models import Raca, Cachorro
from .tasks import adicionar_raca, adicionar_cachorro
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404


class TemplateIndexView(TemplateView):
    template_name = 'index.html'

class TemplateRelatorioRacaView(TemplateView):
    template_name = 'relatorio_raca.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['racas'] = Raca.objects.all()

        search_racas = self.request.GET.get('search_racas')

        if search_racas:
            context['racas'] = Raca.objects.filter(nome__icontains=search_racas)

        return context
    
class TemplateRelatorioCachorroView(TemplateView):
    template_name = 'relatorio_cachorro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cachorros'] = Cachorro.objects.all()
        context['racas'] = Raca.objects.all()

        search_cachorros = self.request.GET.get('search_cachorros')

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
        context['racas'] = Raca.objects.all()
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
        context['cachorros'] = Cachorro.objects.all()
        return context

class EditarRacaView(View):
    def post(self, request):
        raca_id = request.POST['raca_id']
        nome = request.POST['nome']
        cores = request.POST['cores']
        pais = request.POST['pais']
        tamanho = request.POST['tamanho']
        descricao = request.POST['descricao']
        
        raca = get_object_or_404(Raca, id=raca_id)
        raca.nome = nome
        raca.cores = cores
        raca.pais = pais
        raca.tamanho = tamanho
        raca.descricao = descricao
        raca.save()
        
        return JsonResponse({'success': True})
    
class EditarCachorroView(View):
    def post(self, request):
        cachorro_id = request.POST['cachorro_id']
        nome = request.POST['nome']
        peso = request.POST['peso']
        altura = request.POST['altura']
        sexo = request.POST['sexo']
        descricao = request.POST['descricao']
        personalidade = request.POST['personalidade']
        raca_id = request.POST['raca_id']
        
        cachorro = get_object_or_404(Cachorro, id=cachorro_id)
        cachorro.nome = nome
        cachorro.peso = peso
        cachorro.altura = altura
        cachorro.sexo = sexo
        cachorro.descricao = descricao
        cachorro.personalidade = personalidade
        cachorro.raca = get_object_or_404(Raca, id=raca_id)
        cachorro.save()
        
        return JsonResponse({'success': True})
