from django.urls import path
from . import views

app_name =  'tipoatividade'

urlpatterns = [
   path('cadastro/', views.carregar_cadastro , name='cadastro'),
   path('cadastrar/', views.cadastrar , name='cadastrar'),
   path('listar/', views.listar , name='listar'),  
   path('excluir/<int:codigoTipoatividade>', views.excluir, name='excluir_tipoatividade' ),
    
]