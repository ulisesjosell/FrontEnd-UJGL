import streamlit as st
import pandas as pd
import torch
from transformers import pipeline

# 1. Configuración de la página web
st.set_page_config(page_title="Resumen y Análisis IA", page_icon="🤖", layout="centered")

st.title("Registro de Hechiceros e IA 🤖")

# --- PARTE 1: ESTADÍSTICAS (Tu código anterior) ---
st.subheader("Estadísticas del Colegio Técnico de Magia")
data = {
    "Personaje": ["Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki", "Satoru Gojo", "Kento Nanami"],
    "Misiones Completadas": [12, 28, 15, 150, 60],
    "Poder Estimado (Base 100)": [75, 82, 70, 999, 88]
}
df = pd.DataFrame(data)
st.dataframe(df)
st.bar_chart(df.set_index("Personaje")["Poder Estimado (Base 100)"])

st.divider() # Línea separadora

# --- PARTE 2: RESUMIDOR DE IA (Código del profesor) ---
st.subheader("IA: Resumidor de Expedientes")
st.write("Utiliza este modelo de aprendizaje profundo para resumir largos reportes de misiones automáticamente.")

# 2. Cargar el modelo de IA
@st.cache_resource
def cargar_modelo():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

with st.spinner("Cargando el modelo de IA (puede tardar un poco la primera vez)..."):
    resumidor = cargar_modelo()

# 3. Interfaz de usuario (Entrada de datos)
texto_entrada = st.text_area(
    "Pega el texto del expediente que deseas resumir aquí:",
    height=200,
    placeholder="Escribe o pega un reporte largo..."
)

col1, col2 = st.columns(2)
with col1:
    longitud_max = st.slider("Longitud máxima del resumen (palabras)", 30, 150, 75)
with col2:
    longitud_min = st.slider("Longitud mínima del resumen (palabras)", 10, 50, 25)

# 4. Procesamiento
if st.button("Generar Resumen con IA", type="primary"):
    if texto_entrada.strip() == "":
        st.warning("Por favor, ingresa algún texto antes de procesar.")
    elif len(texto_entrada.split()) < 30:
        st.warning("El texto es muy corto. Ingresa al menos 30 palabras.")
    else:
        with st.spinner("La Inteligencia Artificial está procesando el texto..."):
            resultado = resumidor(
                texto_entrada,
                max_length=longitud_max,
                min_length=longitud_min,
                do_sample=False
            )
            resumen_generado = resultado[0]['summary_text']
            
        st.success("¡Resumen generado con éxito!")
        st.write(resumen_generado)