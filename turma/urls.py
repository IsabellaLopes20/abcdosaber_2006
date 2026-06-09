from django.urls import path
from . import views

app_name =  'turma'

urlpatterns = [
     path('cadastro/', views.cadastro , name='cadastro'),   
     path('lista/', views.listar , name='listar'),
     path('registro/', views.registro , name='registro' ),
]