from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Raca

class RacaForm(forms.ModelForm):
    class Meta:
        model = Raca
        fields = ['nome', 'peso', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'Salvar'))
