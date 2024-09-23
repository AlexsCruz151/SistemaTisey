from django.contrib import admin
from apps.catalogos.municipios.models import Municipio

# Register your models here.

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['id','codigo', 'nombre','departamento_nombre']

    def departamento_nombre(self, obj):
        return obj.departamento.nombre

    departamento_nombre.short_description = 'Departamento'