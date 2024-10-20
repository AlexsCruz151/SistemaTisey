from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
from .models import Venta, DetalleVenta, Producto, Cliente, Vendedores
from .serializers import VentaSerializer
from drf_yasg.utils import swagger_auto_schema

class VentaAPIView(APIView):
    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        serializer = VentaSerializer(data=request.data)

        if serializer.is_valid():
            cliente_id = serializer.validated_data.get('cliente').id
            vendedor_id = serializer.validated_data.get('vendedores').id
            detalles_data = serializer.validated_data.get('detalles')

            try:
                with transaction.atomic():
                    cliente = Cliente.objects.get(id=cliente_id)
                    vendedor = Vendedores.objects.get(id=vendedor_id)
                    venta = Venta.objects.create(cliente=cliente, vendedores=vendedor, total=0)
                    total_venta = 0
                    for detalle_data in detalles_data:
                        producto_id = detalle_data['producto'].id  # Obteniendo el ID del producto
                        producto = Producto.objects.get(id=producto_id)  # Obteniendo el objeto completo
                        cantidad = detalle_data['cantidad']

                        if producto.stock < cantidad:
                            return Response(
                                {"Error": f"Stock insuficiente para el producto: {producto.nombre}"},
                                status=status.HTTP_400_BAD_REQUEST
                            )

                        subtotal = producto.precio * cantidad
                        total_venta += subtotal

                        producto.stock -= cantidad
                        producto.save()

                        DetalleVenta.objects.create(
                            venta=venta,
                            producto=producto,
                            cantidad=cantidad,
                            subtotal=subtotal
                        )

                    # Actualiza el total de la venta después de procesar todos los productos
                    venta.total = total_venta
                    venta.save()

                    return Response({
                        'venta_id': venta.id,
                        'cliente': venta.cliente.nombres,
                        'vendedor': vendedor.nombres,
                        'detalles': serializer.data['detalles'],
                        'fecha': venta.fecha
                    }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
