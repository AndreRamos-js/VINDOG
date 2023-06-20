from django.shortcuts import render
from .forms import RacaForm
from .models import Raca

def cadastrar_raca(request):
    form = RacaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RacaForm()
    return render(request, 'racas/cadastrar_raca.html', {'form': form})

def relatorio_racas(request):
    racas = Raca.objects.all()
    return render(request, 'racas/relatorio_racas.html', {'racas': racas})
