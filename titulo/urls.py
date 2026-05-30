from django.urls import path
from . import views

app_name = 'titulo'

urlpatterns = [
    path('lista', views.listar , name='listar'),
    path('lista', views.cadastro , name='cadastro'),
]
