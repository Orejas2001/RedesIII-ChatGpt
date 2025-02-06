import os
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

MODEL_DIR = "./model_files"
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# Función para preprocesar los datos
def preprocess_data(data, fit=False, scaler=None):
    if fit:
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
    else:
        data_scaled = scaler.transform(data)
    return data_scaled, scaler

# Función para entrenar y guardar el modelo
def train_model(X):
    X_scaled, scaler = preprocess_data(X, fit=True)
    joblib.dump(scaler, os.path.join(MODEL_DIR, 'scaler.joblib'))
    
    # Mejor modelo encontrado en la búsqueda manual
    model = IsolationForest(n_estimators=100, max_samples='auto', contamination=0.01, random_state=42)
    model.fit(X_scaled)
    
    # Guardar el modelo entrenado
    joblib.dump(model, os.path.join(MODEL_DIR, 'isolation_forest_model.joblib'))
    print("Modelo y escalador entrenados y guardados exitosamente.")

# Función para detectar anomalías
def detect_anomalies(data):
    # Cargar modelo y escalador
    model = joblib.load(os.path.join(MODEL_DIR, 'isolation_forest_model.joblib'))
    scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.joblib'))

    # Escalar los datos
    data_scaled, _ = preprocess_data(data, fit=False, scaler=scaler)

    # Detectar anomalías
    anomalies = model.predict(data_scaled)  # Devuelve -1 para anomalías, 1 para normales
    anomaly_score = model.decision_function(data_scaled)  # Puntuación de anomalía
    
    # Asegurar que se devuelvan ambos valores: anomalía y puntaje
    is_anomaly = anomalies[0] == -1
    return is_anomaly, anomaly_score[0]

# Ejemplo de entrenamiento
if __name__ == "__main__":
    X = np.random.rand(1000, 3)  # Sustituye por tus datos
    train_model(X)

