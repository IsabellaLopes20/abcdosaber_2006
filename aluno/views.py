from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def aluno(request):
   pagina='Olá, sou a view do app aluno'
   return HttpResponse(pagina)
