# metro_vs_bus_modelo.py

# ========================================
# MÉTODO DE APRENDIZAJE SUPERVISADO: ÁRBOL DE DECISIÓN
# Comparación entre tiempos de viaje en metro y bus
# para predecir el medio de transporte recomendado.
# ========================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('rutas_transporte.csv')

# Convertir los textos de origen y destino en números
le_origen = LabelEncoder()
le_destino = LabelEncoder()
df['origen_cod'] = le_origen.fit_transform(df['origen'])
df['destino_cod'] = le_destino.fit_transform(df['destino'])

# Variables de entrada y salida
X = df[['origen_cod', 'destino_cod', 'tiempo_metro', 'tiempo_bus']]
y = df['medio_recomendado']

# Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# Evaluar el modelo
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

# ------------------------------------------
# Caso de ejemplo: ir de 'El Poblado' a 'Itagüí' con tiempos reales
origen = 'El Poblado'
destino = 'Itagüí'
tiempo_metro = 15
tiempo_bus = 8

# Codificar origen y destino
origen_cod = le_origen.transform([origen])[0]
destino_cod = le_destino.transform([destino])[0]

# Crear DataFrame con nombres de columnas (evita el warning)
nueva_ruta_df = pd.DataFrame([[origen_cod, destino_cod, tiempo_metro, tiempo_bus]],
                              columns=['origen_cod', 'destino_cod', 'tiempo_metro', 'tiempo_bus'])

# Predecir el medio recomendado
prediccion = modelo.predict(nueva_ruta_df)
print(f"Medio recomendado para ir de {origen} a {destino}: {prediccion[0]}")

