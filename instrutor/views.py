from django.shortcuts import render
from django.http import HttpResponse
from instrutor.models import Instrutor

# Create your views here.
def cadastro(request):
  return render(request, 'instrutor/cadastroinstrutor.html')

def listar(request):
  lista_instrutores = Instrutor.objects.all()
  contexto = {
      'instrutores': lista_instrutores
  }
  return render(request, 'instrutor/listarInstrutores.html', context=contexto)