#!/usr/bin/env bash
# Exit on error
set -o errexit
# Instalar el controlador ODBC 17 para SQL Server
# Crear el directorio para almacenar las claves
#mkdir -p /etc/apt/keyrings
#
## Descargar e instalar la clave de Microsoft en el nuevo formato
#curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /etc/apt/keyrings/microsoft.gpg
#
## Agregar el repositorio de Microsoft
#echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/ubuntu/$(lsb_release -rs)/prod focal main" > /etc/apt/sources.list.d/mssql-release.list
#
## Actualizar el repositorio e instalar el controlador ODBC
#apt-get update
#ACCEPT_EULA=Y apt-get install -y msodbcsql17


# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate