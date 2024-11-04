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
import logging
import logging.handlers

# Configura el logger
logger = logging.getLogger(__name__)


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
        logger.info("GET request to list all departamentos")
        departamentos = Departamento.objects.all().order_by('id')
        page = self.paginate_queryset(departamentos,request)

        if page is not None:
            serializer = DepartamentoSerializer(page, many=True)
            logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        serializer = DepartamentoSerializer(departamentos, many=True)
        logger.info("Returning all departamentos without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={201: DepartamentoSerializer})
    def post(self, request):
        """
        Crear un nuevo departamento.
        """
        logger.info("POST request to create a new departamento")

        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Departamento created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("Failed to create departamento: %s", serializer.errors)
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

        logger.info("PUT request to update departamento with ID: %s", pk)

        departamento = get_object_or_404(Departamento, id=pk)
        if not departamento:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, departamento)  # Verificación de permisos
        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Departamento updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.warning("Failed to update departamento with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un departamento por su ID.
        """
        logger.info("PATCH request to partially update departamento with ID: %s", pk)
        departamento = get_object_or_404(Departamento, id=pk)
        if not departamento:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, departamento)  # Verificación de permisos
        serializer = DepartamentoSerializer(departamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Departamento partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.warning("Failed to partially update departamento with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un departamento por su ID.
        """
        logger.info("DELETE request to delete departamento with ID: %s", pk)
        departamento = get_object_or_404(Departamento, id=pk)
        if not departamento:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, departamento)  # Verificación de permisos
        departamento.delete()
        logger.info("Departamento deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)