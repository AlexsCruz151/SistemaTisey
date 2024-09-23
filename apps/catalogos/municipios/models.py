from django.db import models
from apps.catalogos.departamentos.models import Departamento
# Create your models here.
"""
Municipio 
"""
class Municipio(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"