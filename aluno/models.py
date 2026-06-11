from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(
        primary_key=True,
        help_text="Matrícula do aluno"
    )

    nome = models.CharField(
        max_length=70,
        null=False,
        help_text="Informe o nome do aluno"
    )

    

    dataInicial = models.DateField(
        null=False,
        help_text="Informe a data inicial"
    )
    
    dataFinal = models.DateField(
        null=False,
        help_text="Informe a data final"
    )

    

    


    def __str__(self):
        return f'{self.matricula} {self.nome}'