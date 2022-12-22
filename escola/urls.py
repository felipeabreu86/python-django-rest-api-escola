from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from escola.alunos.views import AlunosViewSet
from escola.cursos.views import CursosViewSet
from escola.matriculas.views import ListaAlunosMatriculados, ListaMatriculasAluno, MatriculaViewSet


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matrículas')

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas', ListaAlunosMatriculados.as_view()),
]
