# Detección de Comportamientos Anómalos en Inicios de Sesión

Este proyecto tiene como objetivo detectar comportamientos anómalos durante los inicios de sesión utilizando redes neuronales entrenadas con parámetros específicos. El sistema genera un puntaje ponderado basado en el horario de inicio de sesión, la IP del dispositivo y la ubicación aproximada. Este puntaje se envía a través de una API a ChatGPT, que genera un mensaje personalizado dependiendo del nivel de riesgo detectado.

## Características Principales

- **Detección de Anomalías**: Uso de redes neuronales para analizar patrones de inicio de sesión.
- **Puntaje Ponderado**: Cálculo de un puntaje basado en el horario, IP y ubicación.
- **Integración con ChatGPT**: Envío del puntaje a una API de ChatGPT para generar mensajes personalizados según el riesgo.

## Estructura del Proyecto

- `auth_env/`: Configuraciones relacionadas con la autenticación.
- `model/`: Modelos de redes neuronales entrenados.
- `model_files/`: Archivos relacionados con los modelos.
- `static/`: Archivos estáticos (CSS, JS, imágenes).
- `templates/`: Plantillas para la interfaz de usuario.
- `.env`: Variables de entorno.
- `app.py`: Aplicación principal.

## Requisitos

- Python 3.x
- Librerías especificadas en `requirements.txt`

## Instalación

1. Clona el repositorio:
   git clone:

Crea un entorno virtual:
python -m venv venv
Activa el entorno virtual:

En Windows:

bash
Copy
venv\Scripts\activate
En macOS/Linux:

source venv/bin/activate
Instala las dependencias:

pip install -r requirements.txt
Configura las variables de entorno en el archivo .env.

Uso
Ejecuta la aplicación principal:

python app.py
La aplicación estará disponible en http://localhost:5000.

API Personalizada
La API personalizada se utiliza para enviar el puntaje ponderado a ChatGPT. Asegúrate de configurar correctamente las claves de API y los endpoints en el archivo .env.
