from django.http import HttpResponse
from django.shortcuts import render, redirect
from aluno.models import Aluno

# Create your views here.

def cadastro(request):
  return render(request, 'aluno/cadastroAluno.html')

def listar(request):
  lista_alunos = Aluno.objects.all()
  contexto = {
      'alunos': lista_alunos
  }
  return render(request, 'aluno/listarAlunos.html', context=contexto)


def excluir(request, codigoAluno):
    try: 
        titulo = Aluno.objects.get(pk=codigoAluno)
        titulo.delete()
    except Aluno.DoesNotExist:
        pass
    
    return redirect('aluno:listar')