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
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Departamento
# from .serializers import DepartamentoSerializer
#
# class DepartamentoViewSet(viewsets.ModelViewSet):
#     """
#     A ViewSet for viewing, creating, updating, and deleting Departamento instances.
#     """
#     queryset = Departamento.objects.all()  # Define el conjunto de datos
#     serializer_class = DepartamentoSerializer  # Usa el serializador para los datos
#
#     # Sobrescribir el método create (POST)
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     # Sobrescribir el método retrieve (GET por id)
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     # Sobrescribir el método update (PUT)
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         if getattr(instance, '_prefetched_objects_cache', None):
#             instance._prefetched_objects_cache = {}
#
#         return Response(serializer.data)
#
#     # Sobrescribir el método partial_update (PATCH)
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)
#
#     # Sobrescribir el método destroy (DELETE)
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)




from rest_framework.viewsets import ModelViewSet
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()  # Define el conjunto de datos
    serializer_class = DepartamentoSerializer  # Usa el serializador para los datos
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Departamento
# from .serializers import DepartamentoSerializer
# from rest_framework.decorators import action
#
# class DepartamentoViewSet(ModelViewSet):
#     queryset = Departamento.objects.all()
#     serializer_class = DepartamentoSerializer
#
#     # Sobrescribir el método create para agregar lógica extra
#     def create(self, request, *args, **kwargs):
#         # Agregar lógica extra antes de la creación
#         print("Antes de crear el Departamento")
#
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         # Lógica adicional para validaciones personalizadas o cálculos
#         if some_custom_condition():
#             return Response({'error': 'Custom validation error'}, status=status.HTTP_400_BAD_REQUEST)
#
#         self.perform_create(serializer)
#
#         # Agregar lógica extra después de la creación
#         print("Después de crear el Departamento")
#
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     # Sobrescribir el método update para lógica extra en la actualización
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#
#         # Lógica personalizada antes de la actualización
#         print("Antes de actualizar el Departamento")
#
#         partial = kwargs.pop('partial', False)
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#
#         # Lógica personalizada después de la actualización
#         print("Después de actualizar el Departamento")
#
#         return Response(serializer.data)
#
#     # Sobrescribir el método destroy para agregar lógica antes de eliminar
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#
#         # Agregar lógica antes de la eliminación, por ejemplo, evitar borrar si cumple una condición
#         if instance.is_protected():
#             return Response({'error': 'No se puede eliminar este Departamento'}, status=status.HTTP_400_BAD_REQUEST)
#
#         self.perform_destroy(instance)
#
#         # Agregar lógica después de la eliminación, si es necesario
#         print("Departamento eliminado exitosamente")
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     # Método opcional para agregar lógica personalizada al crear un objeto
#     def perform_create(self, serializer):
#         # Aquí podrías agregar lógica adicional, como notificaciones o crear registros relacionados
#         print("Lógica extra durante la creación")
#         serializer.save()
#
#     # Método opcional para agregar lógica personalizada al actualizar un objeto
#     def perform_update(self, serializer):
#         # Aquí podrías agregar lógica adicional durante la actualización
#         print("Lógica extra durante la actualización")
#         serializer.save()
#
#     # Método opcional para agregar lógica personalizada al eliminar un objeto
#     def perform_destroy(self, instance):
#         # Aquí podrías agregar lógica adicional durante la eliminación
#         print("Lógica extra durante la eliminación")
#         instance.delete()
#
#     @action(detail=False, methods=['get'])
#     def departamentos_activos(self, request):
#         """
#         Método personalizado que devuelve los departamentos activos.
#         """
#         departamentos = Departamento.objects.filter(activo=True)
#         serializer = DepartamentoSerializer(departamentos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @action(detail=True, methods=['post'])
#     def desactivar(self, request, pk=None):
#         """
#         Método personalizado para desactivar un departamento.
#         """
#         departamento = self.get_object()
#         departamento.Codigo = 'False'
#         departamento.save()
#         return Response({'status': 'Departamento desactivado'}, status=status.HTTP_200_OK)
#
# # Función de ejemplo para alguna condición personalizada
# def some_custom_condition():
#     # Aquí podrías implementar alguna validación o lógica adicional
#     return False



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# class DepartamentoActivarView(APIView):
#     """
#     Endpoint personalizado para activar un departamento.
#     """
#     def post(self, request, pk):
#         try:
#             departamento = Departamento.objects.get(pk=pk)
#             #departamento.activo = True
#             #departamento.save()
#             return Response({'status': 'Departamento activado'}, status=status.HTTP_200_OK)
#         except Departamento.DoesNotExist:
#             return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
