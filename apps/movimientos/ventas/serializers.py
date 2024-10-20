from rest_framework.serializers import ModelSerializer

from .models import DetalleVenta,Venta


class DetalleVentaSerializer(ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['producto','cantidad']

class VentaSerializer(ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)
    class Meta:
        model = Venta
        fields = ['cliente','vendedores','detalles']
