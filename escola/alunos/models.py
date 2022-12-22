from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    class Meta:
        verbose_name_plural = 'Alunos'
        verbose_name = 'aluno'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
