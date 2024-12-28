from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Despesa
from .forms import DespesaForm
import pandas as pd
import logging

logger = logging.getLogger(__name__)

@login_required(login_url="login")
def despesa_list(request):
    despesas = Despesa.objects.filter(usuario=request.user)
    df = pd.DataFrame(list(despesas.values('categoria', 'valor')))
    if not df.empty:
        df['valor'] = df['valor'].astype(float)
        total_despesas = df['valor'].sum()
        despesas_por_categoria = df.groupby('categoria')['valor'].sum().to_dict()
    else:
        total_despesas = 0
        despesas_por_categoria = {}
    context = {
        'despesas': despesas,
        'total_despesas': total_despesas,
        'despesas_por_categoria': despesas_por_categoria
    }
    return render(request, 'despesas.html', context)


@login_required(login_url="login")
@require_http_methods(['GET', 'POST'])
def despesa_create(request):
    if request.method == "POST":
        form = DespesaForm(request.POST)
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            messages.success(request, "Despesa criada com sucesso!")
            logger.debug("Despesa criada com sucesso!")
            return redirect('despesa_list')
        else:
            logger.debug("Formulário inválido: %s", form.errors)
    else:
        form = DespesaForm()
    return render(request, 'despesa_form.html', {'form': form})


@login_required(login_url="login")
@require_http_methods(['GET', 'POST'])
def despesa_update(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            messages.success(request, "Despesa atualizada com sucesso!")
            return redirect('despesa_list')
    else:
        form = DespesaForm(instance=despesa)
    return render(request, 'despesa_form.html', {'form': form})


@login_required(login_url="login")
@require_http_methods(['POST'])
def despesa_delete(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk, usuario=request.user)
    despesa.delete()
    messages.success(request, "Despesa deletada com sucesso!")
    return redirect('despesa_list')
