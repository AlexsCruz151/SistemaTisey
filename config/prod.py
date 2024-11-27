from .base import *
import os
from decouple import config
from config.utils.logging_config import ANSIColorFormatter
# SECURITY WARNING: keep the secret key used in production secret!



STATIC_URL = '/static/'
DEBUG = 'RENDER' not in os.environ

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',  # Asegúrate de que este es el backend que estás utilizando
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),

        #"'PORT': '1433',  # Opcional: Puedes omitirlo si usas el puerto predeterminado
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes;',
            'unicode_results': True,  # Opcional: Mejora la compatibilidad con caracteres Unicode
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',  # Utilizamos el backend mssql-django
#         'NAME': os.environ.get('DB_NAME'),  # Nombre de la base de datos
#         'USER': os.environ.get('DB_USER'),  # Usuario de la base de datos
#         'PASSWORD': os.environ.get('DB_PASSWORD'),  # Contraseña de la base de datos
#         'HOST': os.environ.get('DB_HOST'),  # IP del servidor SQL Server
#         #'PORT': '1220',  # Puerto del servidor SQL Server (1433 es el predeterminado)
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',  # Especifica el driver ODBC que tienes instalado
#             'extra_params': 'TrustServerCertificate=yes',  # Útil si estás usando SSL sin un certificado de confianza
#         },
#     }
# }





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
            'address': (os.environ.get('HOST_PAPERTRAIL'), int(os.environ.get('PORT_PAPERTRAIL'))),
        },
    },
    'root': {
        'handlers': ['console', 'papertrail'],
        'level': 'DEBUG',
    },
}

# # Configuración de JWT
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': os.environ.get('SECRET_KEY', default='your secret key'),  # Asegúrate de cambiar esto por una clave secreta real
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
# }
