from rest_framework.viewsets import ModelViewSet
from .models import Departamento
from .serializers import DepartamentoSerializer
from rest_framework.permissions import IsAuthenticated

class DepartamentoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Departamento.objects.all()  # Define el conjunto de datos
    serializer_class = DepartamentoSerializer  # Usa el serializador para los datos