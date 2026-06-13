from django.http import HttpResponse
from django.shortcuts import render
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