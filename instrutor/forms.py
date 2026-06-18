from django import forms
from instrutor.models import Instrutor


class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = [
            'rg',
            'nome',
            'dataNascimento',
            'telefone',
            'ddd',
            'codigoTitulo'
        ]