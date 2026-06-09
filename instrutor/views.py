from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
  return render(request, 'instrutor/cadastroinstrutor.html')

def listar(request):
    return render(request, 'instrutor/listarInstrutores.html')