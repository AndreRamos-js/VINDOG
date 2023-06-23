from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Raca, Cachorro

class RacaForm(forms.ModelForm):
    class Meta:
        model = Raca
        fields = ['nome', 'cores', 'pais', 'tamanho', 'descricao']

    def __init__(self, *args, **kwargs):
        super(RacaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.add_input(Submit('submit', 'Cadastrar'))

class CachorroForm(forms.ModelForm):
    class Meta:
        model = Cachorro
        fields = ['nome', 'peso', 'altura', 'sexo', 'descricao', 'personalidade', 'raca']

    def __init__(self, *args, **kwargs):
        super(CachorroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.add_input(Submit('submit', 'Cadastrar'))
