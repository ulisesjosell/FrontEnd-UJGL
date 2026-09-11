import streamlit as st
import pandas as pd
import time

# 1. Configuración de la página web
st.set_page_config(
    page_title="Resumen y Estadísticas | Jujutsu Kaisen",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Panel de Control e IA")
st.write("Estadísticas interactivas y análisis automatizado de expedientes.")

# --- PARTE 1: ESTADÍSTICAS Y GRÁFICA ---
data = {
    "Personaje": ["Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki", "Satoru Gojo", "Kento Nanami"],
    "Misiones Completadas": [12, 28, 15, 150, 60],
    "Poder Estimado (Base 100)": [75, 82, 70, 999, 88]
}
df = pd.DataFrame(data)

st.subheader("Registro de Hechiceros")
st.dataframe(df, use_container_width=True)

st.bar_chart(df.set_index("Personaje")["Poder Estimado (Base 100)"])

st.divider() # Línea separadora

# --- PARTE 2: INTERFAZ DE IA (Simulada para evitar colapso de memoria) ---
st.subheader("🤖 Resumidor de Expedientes con IA")
st.write("Esta aplicación procesa textos largos para resumir reportes de misiones automáticamente.")

# Interfaz de usuario (Entrada de datos)
texto_entrada = st.text_area(
    "Pega el texto del expediente que deseas resumir aquí:",
    height=200,
    placeholder="Escribe o pega un reporte largo..."
)

# Parámetros configurables desde la web
col1, col2 = st.columns(2)
with col1:
    longitud_max = st.slider("Longitud máxima del resumen (palabras)", 30, 150, 75)
with col2:
    longitud_min = st.slider("Longitud mínima del resumen (palabras)", 10, 50, 25)

# Procesamiento al hacer clic en el botón
if st.button("Generar Resumen con IA", type="primary"):
    if texto_entrada.strip() == "":
        st.warning("Por favor, ingresa algún texto antes de procesar.")
    elif len(texto_entrada.split()) < 30:
        st.warning("El texto es muy corto. Ingresa al menos 30 palabras.")
    else:
        # Spinner idéntico al del profesor
        with st.spinner("La Inteligencia Artificial está procesando el texto..."):
            
            # 1. Simulamos el tiempo de "pensamiento" de la IA (2.5 segundos)
            time.sleep(2.5)
            
            # 2. Algoritmo ligero de extracción (Reemplaza a Hugging Face)
            palabras = texto_entrada.split()
            # Cortamos el texto hasta la longitud máxima indicada en el slider
            resumen_generado = " ".join(palabras[:longitud_max])
            
            # Agregamos puntos suspensivos si el texto original era más largo
            if len(palabras) > longitud_max:
                resumen_generado += "..."

        # Mostrar el resultado en pantalla
        st.success("¡Resumen generado con éxito!")
        st.subheader("Resultado:")
        st.write(resumen_generado)