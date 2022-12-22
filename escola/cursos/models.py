from django.db import models


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(
        max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    class Meta:
        verbose_name_plural = 'Cursos'
        verbose_name = 'curso'
        ordering = ('codigo_curso',)

    def __str__(self):
        return self.descricao
