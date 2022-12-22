from django.contrib import admin
from escola.cursos.models import Curso


class CursoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso', )
    list_per_page = 20


admin.site.register(Curso, CursoModelAdmin)
