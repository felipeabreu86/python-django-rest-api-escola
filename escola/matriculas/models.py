from django.db import models
from escola.alunos.models import Aluno
from escola.cursos.models import Curso


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(
        max_length=1, choices=PERIODO, blank=False, null=False, default='M')
