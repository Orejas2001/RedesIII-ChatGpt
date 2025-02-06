from flask import Flask, jsonify, render_template, redirect, request
import openai
import random

app = Flask(__name__)

# Configuración de la API de OpenAI
openai.api_key = "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"  # Reemplaza esto con tu propia clave de OpenAI

@app.route("/")
def index():
    return redirect("/home")

@app.route("/home")
def home():
    # Permitir que el puntaje de anomalía sea pasado como parámetro para pruebas
    anomaly_score = request.args.get('score', type=float)
    
    # Si no se proporciona un puntaje, se genera uno aleatorio entre 0 y 1
    if anomaly_score is None:
        anomaly_score = round(random.uniform(0.8, 1), 2)
    
    # Crear un mensaje de contexto en función del puntaje de anomalía
    prompt = (
        f"El sistema ha detectado un comportamiento con un puntaje de anomalía de {anomaly_score:.2f}. "
        "Proporciona una respuesta apropiada y contextualizada para este nivel de anomalía."
    )

    try:
        # Solicitar respuesta del modelo de OpenAI usando el contexto del puntaje de anomalía
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente que proporciona respuestas útiles sobre anomalías en un inicio de sesion, de acuerdo a un modelo preentrenado, ten en cuenta que la integridad de la empresa pasa por este login entonces tienes que ser muy cuidadoso."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extraer el mensaje generado por el modelo
        message = response['choices'][0]['message']['content'].strip()
        
        return render_template('home.html', message=message, anomaly_score=anomaly_score)
    
    except openai.error.AuthenticationError:
        return jsonify({"error": "Acceso denegado: API Key no válida"}), 403
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/login", methods=["POST", "GET"])
def login():
    # Redirige a la página principal después del login
    return redirect("/home")

if __name__ == "__main__":
    app.run(debug=True)

