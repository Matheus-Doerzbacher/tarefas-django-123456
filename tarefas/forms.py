from django import forms
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            'titulo',
            'descricao',
        ]

        widgets = {
            'titulo': forms.TextInput(
                attrs={'placeholder': 'Titulo da Tarefa', 'class': 'form-control'}
            ),
            'descricao': forms.TextInput(
                attrs={'placeholder': 'Descrição da tarefa', 'class': 'form-control'}
            ),
        }
