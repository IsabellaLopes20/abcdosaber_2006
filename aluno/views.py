from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cadastro(request):
  return render(request, 'aluno/cadastroAluno.html')

def listar(request):
    return render(request, 'aluno/listarAlunos.html')