from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
       
    path('cadastro/', views.cadastro , name='cadastro'),
    path('listar/', views.listar , name='listar'),
    path('excluir/<int:codigoAluno>', views.excluir, name='excluir_Aluno' ),
]