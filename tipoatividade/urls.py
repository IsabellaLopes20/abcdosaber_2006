from django.urls import path
from . import views

app_name =  'tipoatividade'

urlpatterns = [
   path('cadastro/', views.cadastro , name='cadastro'),
   path('listar/', views.listar , name='listar'),  
   path('excluir/<int:codigoTipoatividade>', views.excluir, name='excluir_tipoatividade' ),
    
]