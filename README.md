# SistemaTisey
Proyecto de facturación desarrollado con Django 

#pasos para correr el proyecto

# 1. Crear entorno Virtual
#conda create --name tiseysistema python=3.2.*

# 2.  Activar el entorno creado
#conda activate tiseysistema

# 3. Instalar paquetes desde el archivo de requerimientos:
#pip install -r requirements.txt

# 4. Aplicar migraciones si es necesario a la bd correspondiente 
#python manage.py migrate

# 5. Correr el server 
#python .\manage.py runserver --settings=config.dev