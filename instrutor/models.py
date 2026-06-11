from django.db import models
from titulo.models import Titulo

# Create your models here.

class Instrutor(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text="Código do instrutor"
    )

    rg = models.CharField(
        max_length=20,
        null=False,
        help_text="Informe o RG do instrutor"
    )

    nome = models.CharField(
        max_length=100,
        null=False,
        help_text="Informe o nome do instrutor"
    )

    dataNascimento = models.DateField(
        null=False,
        help_text="Informe a data de nascimento"
    )

    telefone = models.CharField(
        max_length=15,
        null=False,
        help_text="Informe o telefone"
    )

    ddd = models.CharField(
        max_length=2,
        null=False,
        help_text="Informe o DDD"
    )

    codigoTitulo = models.ForeignKey(
        Titulo, 
        null=True,
        blank = True,
        related_name = 'titulos',
        on_delete= models.SET_NULL,
        db_column ="codigoTitulo",
        help_text="Informe o código do título"
    )

    def __str__(self):
        return f'{self.id} {self.nome}'