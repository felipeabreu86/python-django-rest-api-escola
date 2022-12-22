from rest_framework import viewsets
from escola.cursos.models import Curso
from escola.cursos.serializer import CursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

allowed_http_methods = ['get', 'post', 'put', 'patch', 'delete']


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = allowed_http_methods
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
