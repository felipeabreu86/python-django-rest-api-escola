from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

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


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno(a)"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando aluno(a)s matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
