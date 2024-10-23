from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'mssql',  # Utilizamos el backend mssql-django
        'NAME': config('DB_NAME'),  # Nombre de la base de datos
        'USER': config('DB_USER'),  # Usuario de la base de datos
        'PASSWORD': config('DB_PASSWORD'),  # Contraseña de la base de datos
        'HOST': config('DB_HOST'),  # IP del servidor SQL Server
        #'PORT': '1220',  # Puerto del servidor SQL Server (1433 es el predeterminado)
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Especifica el driver ODBC que tienes instalado
            'extra_params': 'TrustServerCertificate=yes',  # Útil si estás usando SSL sin un certificado de confianza
        },
    }
}
