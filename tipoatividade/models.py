from django.db import models

# Create your models here.
class Tipoatividade(models.Model):
    codigo = models.AutoField(
        primary_key=True,
        help_text="Código do tipo atividade"
    )
    
    descricao = models.CharField(
        max_length=70,
        null=False,
        help_text="Informe o tipo de atividade"
    )
    
    def __str__(self):
        return f'{self.codigo} {self.descricao}'