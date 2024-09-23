from rest_framework.serializers import ModelSerializer

from apps.catalogos.departamentos.models import Departamento


class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['codigo', 'nombre']
        #fields = '__all__'
