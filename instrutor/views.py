from django.shortcuts import render
from django.http import HttpResponse
from instrutor.forms import InstrutorForm
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

def carregar_cadastro(request):
  return render(request, 'instrutor/cadastroInstrutores.html')  

def cadastrar(request):
    form= InstrutorForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Instrutor(
            descricao=dados_titulo['descricao']
        )
        titulo.save()
    return render(request, 'instrutor/cadastroInstrutores.html')  
