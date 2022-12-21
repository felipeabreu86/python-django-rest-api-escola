from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


class AlunoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 20


class CursoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso', )
    list_per_page = 20


class MatriculaModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)


admin.site.register(Aluno, AlunoModelAdmin)
admin.site.register(Curso, CursoModelAdmin)
admin.site.register(Matricula, MatriculaModelAdmin)
