from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

@app.route('/', methods=['GET', 'POST'])
def index():
    respuesta = None
    if request.method == 'POST':
        pregunta = request.form['pregunta']
        response = requests.post(f"{BACKEND_URL}/procesar_consulta/", json={"pregunta": pregunta})
        if response.status_code == 200:
            data = response.json()
            respuesta = data['respuesta']
        else:
            respuesta = f"Error: {response.text}"
    return render_template('index.html', respuesta=respuesta)
