from django.db import models

# Create your models here.
"""
Departamentos 
"""
class Departamento(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    class Meta:
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"