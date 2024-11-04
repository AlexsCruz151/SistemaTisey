from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Departamento
from .serializers import DepartamentoSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from ...permissions import CustomPermission
from rest_framework.pagination import PageNumberPagination


class PaginationMixin:
    pagination_class = PageNumberPagination

    def paginate_queryset(self, queryset, request, view=None):
        self.paginator = self.pagination_class()
        self.paginator.page_size = 10  # Puedes definirlo en settings si prefieres
        return self.paginator.paginate_queryset(queryset, request, view=view)

    def get_paginated_response(self, data):
        return self.paginator.get_paginated_response(data)
class DepartamentoApiView(PaginationMixin,APIView):
    """
    Vista para listar todos los departamentos o crear un nuevo departamento.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Departamento  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(responses={200: DepartamentoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los departamentos.
        """
        departamentos = Departamento.objects.all()
        page = self.paginate_queryset(departamentos,request)

        if page is not None:
            serializer = DepartamentoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

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
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Departamento
    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def put(self, request, pk):
        """
        Actualizar completamente un departamento por su ID.
        """
        departamento = get_object_or_404(Departamento, id=pk)
        if not departamento:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, departamento)  # Verificación de permisos
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
        departamento = get_object_or_404(Departamento, id=pk)
        if not departamento:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, departamento)  # Verificación de permisos
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
        departamento = get_object_or_404(Departamento, id=pk)
        if not departamento:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, departamento)  # Verificación de permisos
        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)