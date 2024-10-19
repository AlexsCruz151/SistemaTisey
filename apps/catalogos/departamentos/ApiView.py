from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Departamento
from .serializers import DepartamentoSerializer
from drf_yasg.utils import swagger_auto_schema

class DepartamentoApiView(APIView):
    """
    Vista para listar todos los departamentos o crear un nuevo departamento.
    """

    @swagger_auto_schema(responses={200: DepartamentoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los departamentos.
        """
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={201: DepartamentoSerializer})
    def post(self, request):
        """
        Crear un nuevo departamento.
        """
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoDetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un departamento específico.
    """

    @swagger_auto_schema(responses={200: DepartamentoSerializer})
    def get(self, request, pk):
        """
        Obtener un departamento específico por su ID.
        """
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un departamento por su ID.
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

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un departamento por su ID.
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

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un departamento por su ID.
        """
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from django.urls import path
# from .views import DepartamentoApiView,DepartamentoDetails
#
# urlpatterns = [
#     path('', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('<int:pk>', DepartamentoDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]