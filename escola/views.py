from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

allowed_http_methods = ['get', 'post', 'put', 'patch', 'delete']


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os aluno(a)s"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    http_method_names = allowed_http_methods


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = allowed_http_methods


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = allowed_http_methods
