from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from .forms import RacaForm
from .models import Raca
from django.http import HttpResponseRedirect

class CadastrarRacaView(View):
    template_name = 'cadastrar_raca.html'
    form_class = RacaForm

    def get(self, request):
        form = self.form_class()
        racas = Raca.objects.all()
        return render(request, self.template_name, {'form': form, 'racas': racas})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cadastrar_raca'))  # Redireciona após o salvamento
        racas = Raca.objects.all()
        return render(request, self.template_name, {'form': form, 'racas': racas})
