from rest_framework.viewsets import ModelViewSet
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(ModelViewSet):
    """
    Un ViewSet que maneja las operaciones CRUD para el modelo Departamento.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
