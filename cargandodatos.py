import pandas as pd

# Cargar datos con ruta relativa
df = pd.read_csv('data/archivo.csv')

import streamlit as st
import joblib

# Cargar el modelo entrenado
modelo_entrenado = joblib.load('modelo_entrenado.joblib')

# Título de la aplicación
st.title("Aplicación para predicción de ACV")

# Crear las opciones para las entradas del usuario
# Género
opciones_genero = ["Female", "Male"]
genero = st.selectbox("Selecciona el género con el que te sientes identificado", opciones_genero)

# Hipertensión (0 = No, 1 = Sí)
hipertension = st.selectbox("Pon 0 si no tienes hipertensión o 1 si tienes", ["0", "1"])

# Cardiopatía (0 = No, 1 = Sí)
cardiopatia = st.selectbox("Selecciona 1 si padeces alguna cardiopatía o 0 si no", ["0", "1"])

# Hábito de fumar
opciones_fumar = ["Never smoked", "Smokes", "No smokes", "Formerly smoked"]
humo = st.selectbox("Selecciona el hábito de consumo de tabaco que posees", opciones_fumar)

# Edad (valor numérico)
edad = st.slider("Selecciona tu edad:", min_value=1, max_value=100, value=25)

# IMC (Índice de masa corporal)
imc = st.slider("Selecciona tu IMC:", min_value=10, max_value=100, value=20)

# Convertir las entradas a valores numéricos
# Convertir género en 1 o 0
genero_valor = 1 if genero == "Female" else 0

# Convertir hipertensión y cardiopatía a 0 o 1
hipertension_valor = int(hipertension)
cardiopatia_valor = int(cardiopatia)

# Convertir hábito de fumar en valores numéricos
if humo == "Never smoked":
    never_smoked = 1
    no_smokes = 0
    formerly_smoked = 0
    smokes = 0
elif humo == "No smokes":
    never_smoked = 0
    no_smokes = 1
    formerly_smoked = 0
    smokes = 0
elif humo == "Formerly smoked":
    never_smoked = 0
    no_smokes = 0
    formerly_smoked = 1
    smokes = 0
else:  # "Smokes"
    never_smoked = 0
    no_smokes = 0
    formerly_smoked = 0
    smokes = 1

# Asegurarse de que las entradas sean números
caracteristicas = [
    float(edad),  # Convertir edad a flotante
    int(hipertension_valor),  # Hipertensión como entero
    int(cardiopatia_valor),  # Cardiopatía como entero
    float(imc),  # Convertir IMC a flotante
    int(genero_valor),  # Género como entero
    int(formerly_smoked),  # Fumar anteriormente como entero
    int(never_smoked),  # Nunca fumado como entero
    int(no_smokes),  # No fuma como entero
    int(smokes)  # Fuma como entero
]

# Realizar la predicción
prediccion = modelo_entrenado.predict([caracteristicas])[0]

# Mostrar el resultado de la predicción
if prediccion == 0:
    st.write("No tienes riesgo de sufrir ACV.")
else:
    st.write("Tienes riesgo de sufrir ACV.")


