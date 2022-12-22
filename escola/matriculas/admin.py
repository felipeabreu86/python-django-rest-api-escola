from django.contrib import admin
from escola.matriculas.models import Matricula


class MatriculaModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)


admin.site.register(Matricula, MatriculaModelAdmin)
