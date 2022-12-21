from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

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
