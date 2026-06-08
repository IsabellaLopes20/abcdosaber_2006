from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    return render(request, 'tipoatividade/cadastroTipoatividade.html')
    return HttpResponse("<p>Olá, sou a view do app Tipo de Atividade!</p>")


def listar(request):
    return render(request, 'tipoatividade/listarTiposAtividade.html')
    return HttpResponse("<p>Olá, sou a view do app Tipo de Atividade!</p>")
