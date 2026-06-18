from django.shortcuts import render, redirect
from django.http import HttpResponse
from titulo.forms import TituloForm
from tipoatividade.models import Tipoatividade

# Create your views here.

    

def carregar_cadastro(request):
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')

def cadastrar(request):
    form= TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Tipoatividade(
            descricao=dados_titulo['descricao']
        )
        titulo.save()
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')

def listar(request):
    lista_tipo_atividades = Tipoatividade.objects.all()
    contexto = {
        'tipo_atividades': lista_tipo_atividades
    }
    return render(request, 'tipoatividade/listarTiposAtividade.html', context=contexto)
  
def excluir(request, codigoTipoatividade):
    try: 
        titulo = Tipoatividade.objects.get(pk=codigoTipoatividade)
        titulo.delete()
    except Tipoatividade.DoesNotExist:
        pass
    
    return redirect('tipoatividade:listar')