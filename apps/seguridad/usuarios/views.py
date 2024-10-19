from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from drf_yasg.utils import swagger_auto_schema

class UserCreateView(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        # Validar los datos
        if serializer.is_valid():
            serializer.save()  # Crear el usuario
            return Response({"message": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)

        # En caso de error, retornar las validaciones
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
