from django.shortcuts import render, get_object_or_404
from .forms import RacaForm
from .models import Raca

def cadastrar_raca(request):
    form = RacaForm(request.POST or None)
    if form.is_valid():
        form.save()
    racas = Raca.objects.all()
    return render(request, 'cadastrar_raca.html', {'form': form, 'racas': racas})
