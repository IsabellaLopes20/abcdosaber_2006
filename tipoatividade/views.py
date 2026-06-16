from django.shortcuts import render, redirect
from django.http import HttpResponse
from tipoatividade.models import Tipoatividade

# Create your views here.
def cadastro(request):
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