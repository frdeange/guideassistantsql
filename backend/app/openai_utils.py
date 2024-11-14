import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Configurar OpenAI
openai.api_type = "azure"
openai.api_base = "https://tu-recurso-openai.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("OPENAI_API_KEY")

def generar_consulta_sql(pregunta_usuario):
    prompt = f"""
Eres un asistente que ayuda a generar consultas SQL para SQL Server.
Esquema de la base de datos:
- Tabla 'Clientes' con columnas 'Id', 'Nombre', 'Apellido', 'Email'
- Tabla 'Pedidos' con columnas 'Id', 'ClienteId', 'Fecha', 'Monto'

Genera una consulta SQL para la siguiente solicitud del usuario: '{pregunta_usuario}'.
La consulta debe ser segura y evitar inyecciones SQL.
"""
    response = openai.Completion.create(
        engine="tu-nombre-de-deployment",  # Reemplaza con el nombre de tu deployment
        prompt=prompt,
        max_tokens=150,
        temperature=0.5,
    )
    sql_query = response.choices[0].text.strip()
    return sql_query
