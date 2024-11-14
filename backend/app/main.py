from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai_utils import generar_consulta_sql
from sql_utils import ejecutar_consulta_sql

app = FastAPI()

class Consulta(BaseModel):
    pregunta: str

@app.post("/procesar_consulta/")
async def procesar_consulta(consulta: Consulta):
    try:
        # Generar consulta SQL
        sql_query = generar_consulta_sql(consulta.pregunta)
        
        # Ejecutar consulta SQL
        resultados = ejecutar_consulta_sql(sql_query)
        
        # Componer respuesta
        respuesta = f"Resultados: {resultados}"
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
