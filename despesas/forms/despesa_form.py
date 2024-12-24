from django import forms
from ..models import Despesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['usuario', 'categoria', 'valor', 'descricao']
        widgets = {
            'usuario': forms.HiddenInput(),  # Esconde o campo de usuário no formulário
            'categoria': forms.Select(choices=Despesa.CATEGORIAS),
            'valor': forms.NumberInput(attrs={'step': '0.01'}),
            'descricao': forms.TextInput(attrs={'maxlength': 255}),
        }
