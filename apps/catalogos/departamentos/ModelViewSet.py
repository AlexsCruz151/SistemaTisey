from rest_framework.viewsets import ModelViewSet
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoModelViewSet(ModelViewSet):

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DepartamentoModelViewSet
#
# router = DefaultRouter()
# router.register('', DepartamentoModelViewSet, basename='departamento')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
