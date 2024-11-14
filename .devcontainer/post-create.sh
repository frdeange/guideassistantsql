#!/usr/bin/env bash

set -e

echo "Instalando dependencias del backend..."
pip install -r backend/requirements.txt

echo "Instalando dependencias del frontend..."
pip install -r frontend/requirements.txt

echo "Esperando a que SQL Server se inicie..."
# Esperar a que SQL Server esté listo para aceptar conexiones
sleep 15

echo "Inicializando la base de datos..."
# Ejecutar el script de inicialización de la base de datos
/opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P 'TuPassword123' -i database/init_db.sql

echo "Entorno de desarrollo listo."
