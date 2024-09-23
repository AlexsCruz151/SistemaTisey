from django.contrib import admin
from apps.catalogos.tipoSalidas.models import TipoSalida
# Register your models here.
@admin.register(TipoSalida)
class TipoSalidaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'codigo','descripcion']
    list_display = ['codigo','descripcion']
    list_filter = ['estado']
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(estado=1)  # Filtra solo los tipos de salida que estén activos

    def delete_model(self, request, obj):
        obj.estado = 0  # Establece el estado como inactivo en lugar de eliminar físicamente el objeto
        obj.save()
