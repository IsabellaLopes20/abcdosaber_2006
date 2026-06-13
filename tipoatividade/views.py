from django.shortcuts import render
from django.http import HttpResponse
from tipoatividade.models import Tipoatividade

# Create your views here.
def cadastro(request):
    return render(request, 'tipoatividade/cadastroTiposAtividade.html')
    return HttpResponse("<p>Olá, sou a view do app Tipo de Atividade!</p>")


def listar(request):
    lista_tipo_atividades = Tipoatividade.objects.all()
    contexto = {
        'tipo_atividades': lista_tipo_atividades
    }
    return render(request, 'tipoatividade/listarTiposAtividade.html', context=contexto)
    return HttpResponse("<p>Olá, sou a view do app Tipo de Atividade!</p>")
