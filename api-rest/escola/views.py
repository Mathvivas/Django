from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer
from escola.serializers import ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# viewsets são usados para implementar CRUD
class EstudanteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

# generics são usados para implementar visualizações
class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        # self.kwargs pega todas as infos que são passadas na url
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        # self.kwargs pega todas as infos que são passadas na url
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer