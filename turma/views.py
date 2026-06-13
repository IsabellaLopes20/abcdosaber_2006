from django.shortcuts import render
from django.http import HttpResponse
from turma.models import Turma

# Create your views here.
def cadastro(request):
    return render(request, 'turma/cadastroTurma.html')

def listar(request):
    lista_turmas = Turma.objects.all()
    contexto = {
        'turmas': lista_turmas
    }
    return render(request, 'turma/listarTurmas.html', context=contexto)

def registro(request):
    return render(request, 'turma/registroAusencia.html')

