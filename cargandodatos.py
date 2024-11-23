import pandas as pd

# Cargar datos con ruta relativa
#df = pd.read_csv('data/archivo.csv')

import streamlit as st
import joblib

# Cargar el modelo entrenado
modelo_entrenado = joblib.load('modelo_entrenado.joblib')

# Título de la aplicación
st.title("Aplicación para predicción de ACV")

# Crear las opciones para las entradas del usuario
# Género
opciones_genero = ["Femenino", "Masculino"]
genero = st.selectbox("Selecciona el género con el que te sientes identificado", opciones_genero)

hipertension = st.radio(
    "¿Usted padece hipertensión?",  # Etiqueta para el input
    ["Sí, tengo hipertensión", "No, no tengo hipertensión"]  # Opciones
)

cardiopatia = st.radio(
    "¿Usted tiene alguna cardiopatía?",  # Etiqueta para el input
    ["Sí, padezco de cardiopatía", "No, no padezco de cardiopatías"]  # Opciones
)
# Hábito de fumar
opciones_fumar = ["Nunca fumé", "Fumo", "No fumo", "Antiguamente fumaba"]
humo = st.selectbox("Selecciona el hábito de consumo de tabaco que posees", opciones_fumar)

# Edad (valor numérico)
edad = st.slider("Selecciona tu edad:", min_value=1, max_value=82, value=25)

# IMC (Índice de masa corporal)
imc = st.slider("Selecciona tu IMC:", min_value=10, max_value=98, value=20)

# Convertir las entradas a valores numéricos
# Convertir género en 1 o 0
genero_valor = 1 if genero == "Femenino" else 0


if hipertension == "Sí, tengo hipertensión":
    hipertension_val = 1
else:
    hipertension_val = 0
if  cardiopatia == "Sí, padezco de cardiopatía":
    cardiopatia_valor = 1
else:
    cardiopatia_valor = 0
# Convertir hábito de fumar en valores numéricos
if humo == "Nunca fumé":
    never_smoked = 1
    no_smokes = 0
    formerly_smoked = 0
    smokes = 0
elif humo == "No fumo":
    never_smoked = 0
    no_smokes = 1
    formerly_smoked = 0
    smokes = 0
elif humo == "Antiguamente fumaba":
    never_smoked = 0
    no_smokes = 0
    formerly_smoked = 1
    smokes = 0
else:  
    never_smoked = 0
    no_smokes = 0
    formerly_smoked = 0
    smokes = 1


# Asegurarse de que las entradas sean números
caracteristicas = [
    float(edad),  # Convertir edad a flotante
    int(hipertension_val),  # Hipertensión como entero
    int(cardiopatia_valor),  # Cardiopatía como entero
    float(imc),  # Convertir IMC a flotante
    int(genero_valor),  # Género como entero
    int(formerly_smoked),  # Fumar anteriormente como entero
    int(never_smoked),  # Nunca fumado como entero
    int(no_smokes),  # No fuma como entero
    int(smokes)  # Fuma como entero
]

if st.button("Determinar riesgo de ACV"):
    # Llamar al modelo para predecir
    prediccion = modelo_entrenado.predict([caracteristicas])[0]
    # Mostrar el resultado de la predicción
    if prediccion == 0:
        st.success("No tienes riesgo de sufrir ACV.")
    else:
        st.warning("Tienes riesgo de sufrir ACV.")



