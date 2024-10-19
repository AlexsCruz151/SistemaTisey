
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Departamento
from .serializers import DepartamentoSerializer
from drf_yasg.utils import swagger_auto_schema

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar, crear, obtener, actualizar y eliminar departamentos.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


    # @swagger_auto_schema(responses={200: DepartamentoSerializer(many=True)})
    def list(self, request):
        """
        Listar todos los departamentos.
        """
        return super().list(request)

   # @swagger_auto_schema(request_body=DepartamentoSerializer, responses={201: DepartamentoSerializer})
    def create(self, request):
        """
        Crear un nuevo departamento.
        """
        return super().create(request)

    #@swagger_auto_schema(responses={200: DepartamentoSerializer})
    def retrieve(self, request, pk=None):
        """
        Obtener un departamento específico por su ID.
        """
        return super().retrieve(request, pk)

    #@swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def update(self, request, pk=None):
        """
        Actualizar completamente un departamento por su ID.
        """
        return super().update(request, pk)

   # @swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def partial_update(self, request, pk=None):
        """
        Actualizar parcialmente un departamento por su ID.
        """
        return super().partial_update(request, pk)

   # @swagger_auto_schema(responses={204: 'No Content'})
    def destroy(self, request, pk=None):
        """
        Eliminar un departamento por su ID.
        """
        return super().destroy(request, pk)

# from django.urls import path, include
#
# urlpatterns = [
#
#     path('departamentos/', include('apps.catalogos.departamentos.urls')),
#     path('municipios/', include('apps.catalogos.municipios.urls')),
# ]


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Departamento
from .serializers import DepartamentoSerializer
from drf_yasg.utils import swagger_auto_schema

class DepartamentoViewSet(viewsets.ViewSet):
    """
    Un ViewSet básico que maneja las operaciones CRUD manualmente.
    """

    @swagger_auto_schema(responses={200: DepartamentoSerializer(many=True)})
    def list(self, request):
        """
        GET /departamentos/
        Devuelve la lista de todos los departamentos.
        """
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """
        GET /departamentos/{id}/
        Devuelve un departamento específico por ID.
        """
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)

    def create(self, request):
        """
        POST /departamentos/
        Crea un nuevo departamento.
        """
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """
        PUT /departamentos/{id}/
        Actualiza completamente un departamento existente.
        """
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        """
        PATCH /departamentos/{id}/
        Actualización parcial de un departamento.
        """
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartamentoSerializer(departamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        DELETE /departamentos/{id}/
        Elimina un departamento existente.
        """
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DepartamentoViewSet
#
# router = DefaultRouter()
# router.register('', DepartamentoViewSet, basename='departamento')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
