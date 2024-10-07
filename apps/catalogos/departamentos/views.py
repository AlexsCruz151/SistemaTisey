# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Departamento
# from .serializers import DepartamentoSerializer
#
# class DepartamentoApiView(APIView):
#
#     def get(self, request, pk=None):
#         # Si se proporciona el pk, obtenemos un solo departamento, de lo contrario, todos los departamentos
#         if pk:
#             try:
#                 departamento = Departamento.objects.get(pk=pk)
#             except Departamento.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Departamento no encontrado"})
#             serialize = DepartamentoSerializer(departamento)
#             return Response(status=status.HTTP_200_OK, data=serialize.data)
#         else:
#             departamentos = Departamento.objects.all()
#             serialize = DepartamentoSerializer(departamentos, many=True)
#             return Response(status=status.HTTP_200_OK, data=serialize.data)
#
#     def post(self, request):
#         serialize = DepartamentoSerializer(data=request.data)
#         # Validar los datos enviados en el request
#         if serialize.is_valid(raise_exception=True):
#             serialize.save()  # Guardar el nuevo departamento
#             return Response(status=status.HTTP_201_CREATED, data=serialize.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)
#
#     def put(self, request, pk):
#         try:
#             departamento = Departamento.objects.get(pk=pk)
#         except Departamento.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Departamento no encontrado"})
#
#         # Actualizar los datos del departamento
#         serialize = DepartamentoSerializer(departamento, data=request.data)
#         if serialize.is_valid(raise_exception=True):
#             serialize.save()
#             return Response(status=status.HTTP_200_OK, data=serialize.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)
#
#     def patch(self, request, pk):
#         try:
#             departamento = Departamento.objects.get(pk=pk)
#         except Departamento.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Departamento no encontrado"})
#
#         # Actualización parcial, solo actualiza los campos proporcionados
#         serialize = DepartamentoSerializer(departamento, data=request.data, partial=True)
#         if serialize.is_valid(raise_exception=True):
#             serialize.save()
#             return Response(status=status.HTTP_200_OK, data=serialize.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serialize.errors)
#
#     def delete(self, request, pk):
#         try:
#             departamento = Departamento.objects.get(pk=pk)
#         except Departamento.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Departamento no encontrado"})
#
#         departamento.delete()  # Eliminar el departamento
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting Departamento instances.
    """
    queryset = Departamento.objects.all()  # Define el conjunto de datos
    serializer_class = DepartamentoSerializer  # Usa el serializador para los datos

    # Sobrescribir el método create (POST)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Sobrescribir el método retrieve (GET por id)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Sobrescribir el método update (PUT)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # Sobrescribir el método partial_update (PATCH)
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # Sobrescribir el método destroy (DELETE)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
