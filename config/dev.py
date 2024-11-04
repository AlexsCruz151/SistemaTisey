from .base import *
from decouple import config
from config.utils.logging_config import ANSIColorFormatter




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





# Configura los detalles de conexión a Papertrail
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'custom_format': {
            '()': ANSIColorFormatter,
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom_format',  # Usa el formato personalizado
        },
        'papertrail': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'custom_format',  # Usa el formato personalizado para Papertrail
            'address': (config('HOST_PAPERTRAIL'), int(config('PORT_PAPERTRAIL'))),
        },
    },
    'root': {
        'handlers': ['console', 'papertrail'],
        'level': 'DEBUG',
    },
}