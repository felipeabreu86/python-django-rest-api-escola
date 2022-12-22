from rest_framework import viewsets
from escola.alunos.models import Aluno
from escola.alunos.serializer import AlunoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

allowed_http_methods = ['get', 'post', 'put', 'patch', 'delete']


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os aluno(a)s"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    http_method_names = allowed_http_methods
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
