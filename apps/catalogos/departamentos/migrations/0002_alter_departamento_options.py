# Generated by Django 4.2 on 2024-10-28 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'permissions': [('puede_aprobar', 'Puede aprobar registros'), ('puede_rechazar', 'Puede rechazar registros')], 'verbose_name_plural': 'Departamentos'},
        ),
    ]
