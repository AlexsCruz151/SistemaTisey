from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.catalogos.municipios.models import Municipio


class MunicipiosApiView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK,data='hola desde municipio')

# Create your views here.
