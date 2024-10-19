from rest_framework.viewsets import ModelViewSet
from .models import Departamento
from .serializers import DepartamentoSerializer
from rest_framework.permissions import IsAuthenticated

class DepartamentoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
