from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Tarefa
from .forms import TarefaForm


def index_view(request):
    tarefas = Tarefa.objects.all()
    context = {
        'title': 'Tarefas',
        'tarefas': tarefas,
    }
    return render(request, 'tarefas/index.html', context)


def adicionar_view(request):
    form_action = reverse('adicionar')
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TarefaForm()

    context = {
        'form_action': form_action,
        'form': form,
        'title': 'Adicionar Tarefa',
    }
    return render(request, 'tarefas/adicionar.html', context)


def excluir_view(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    tarefa.delete()
    return redirect('index')
