from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DepartamentoSerializer
from django.shortcuts import get_object_or_404

from apps.catalogos import departamentos
from apps.catalogos.departamentos.models import Departamento


class DepartamentoApiView(APIView):
    def get1(self, request):
      #departamentos = [de.codigo for de in Departamento.objects.all()]
      departamentos = list(Departamento.objects.values())
      return Response(status=status.HTTP_200_OK,data=departamentos)
      #return Response(status=status.HTTP_200_OK,data={'departamentos': Departamento.objects.all()})

    def get(self, request):
        serialize = DepartamentoSerializer(Departamento.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serialize.data)

    def post1(self, request):
        # departamento = Departamento()
        # departamento.codigo = request.data['codigo']
        # departamento.nombre = request.data['nombre']
        # departamento.save()
        Departamento.objects.create(codigo=request.data['codigo'], nombre=request.data['nombre'])
        return Response(status=status.HTTP_201_CREATED)

    def post(self, request):
        serialize=DepartamentoSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_201_CREATED,data=serialize.data)

    def put(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Departamento no encontrado"})

        serialize = DepartamentoSerializer(departamento, data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_200_OK, data=serialize.data)

    def delete(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Departamento no encontrado"})

        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Departamento no encontrado"})

        serialize = DepartamentoSerializer(departamento, data=request.data, partial=True)  # Permite actualizar solo los campos proporcionados
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_200_OK, data=serialize.data)


class DepartamentoApiView2(APIView):
    # Obtener lista de departamentos o filtrar por nombre
    def get(self, request):
        # Filtrar por nombre si se proporciona en los parámetros de consulta
        nombre = request.query_params.get('nombre', None)
        if nombre:
            departamentos = Departamento.objects.filter(nombre__icontains=nombre)  # Filtrar por nombre (contiene)
        else:
            departamentos = Departamento.objects.all()  # Obtener todos los departamentos

        serialize = DepartamentoSerializer(departamentos, many=True)
        return Response(status=status.HTTP_200_OK, data=serialize.data)

    # Crear un nuevo departamento
    def post(self, request):
        serialize = DepartamentoSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_201_CREATED, data=serialize.data)

    # Actualizar completamente un departamento (PUT)
    def put(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)  # Buscar el departamento por ID
        serialize = DepartamentoSerializer(departamento, data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_200_OK, data=serialize.data)

    # Actualizar parcialmente un departamento (PATCH)
    def patch(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)  # Buscar el departamento por ID
        serialize = DepartamentoSerializer(departamento, data=request.data, partial=True)  # Permitir actualización parcial
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(status=status.HTTP_200_OK, data=serialize.data)

    # Eliminar un departamento
    def delete(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)  # Buscar el departamento por ID
        departamento.delete()  # Eliminar el departamento
        return Response(status=status.HTTP_204_NO_CONTENT)  # No se devuelve contenido en la respuesta



