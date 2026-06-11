from django.db import models
from titulo.models import Titulo
# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(
        primary_key=True,
        help_text="Número da turma"
    )

    horarioAula = models.TimeField(
        null=False,
        help_text="Horário da aula"
    )

    duracaoAula = models.IntegerField(
        null=False,
        help_text="Duração da aula em minutos"
    )

    dataInicial = models.DateField(
        null=False,
        help_text="Data inicial da turma"
    )

    dataFinal = models.DateField(
        null=False,
        help_text="Data final da turma"
    )

    matriculaMonitor = models.IntegerField(
        null=False,
        help_text="Matrícula do monitor"
    )

    idInstrutor = models.IntegerField(
        null=False,
        help_text="ID do instrutor"
    )
    
    codigoTitulo = models.ForeignKey(
        Titulo,
        null = True,
        blank = True,
        related_name = 'turma',
        on_delete = models.SET_NULL,
        db_column = "codigoTitulo",
        help_text = "Informe o código do título"
    )
   
   
    def __str__(self):
        return f'Turma {self.numero}'