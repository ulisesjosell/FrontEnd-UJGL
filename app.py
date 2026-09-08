import streamlit as st
import pandas as pd

# 1. Configuración de la página web
st.set_page_config(
    page_title="Resumen y Estadísticas | Jujutsu Kaisen",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Panel de Control - Hechiceros")
st.write("Estadísticas interactivas del Colegio Técnico de Magia Metropolitana.")

# 2. Datos y Tabla interactiva
data = {
    "Personaje": ["Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki", "Satoru Gojo", "Kento Nanami"],
    "Misiones Completadas": [12, 28, 15, 150, 60],
    "Poder Estimado (Base 100)": [75, 82, 70, 999, 88]
}
df = pd.DataFrame(data)

st.subheader("Registro de Hechiceros")
st.dataframe(df, use_container_width=True)

# 3. Gráfica de Poder
st.subheader("Gráfica de Poder")
st.bar_chart(df.set_index("Personaje")["Poder Estimado (Base 100)"])

# 4. Sección interactiva limpia (Simulador de Análisis)
st.divider()
st.subheader("🔍 Buscador y Filtro de Expedientes")
busqueda = st.text_input("Buscar personaje en el registro:")

if busqueda:
    resultado = df[df["Personaje"].str.contains(busqueda, case=False, na=False)]
    if not resultado.empty:
        st.success("¡Coincidencia encontrada!")
        st.dataframe(resultado)
    else:
        st.warning("No se encontró ningún hechicero con ese nombre.")
else:
    st.info("Escribe el nombre de un personaje arriba para filtrar los datos.")