import streamlit as st
import pandas as pd

# Título de la app
st.title("Resumen de Información: Jujutsu Kaisen")
st.write("Estadísticas interactivas del Colegio Técnico de Magia.")

# Datos de ejemplo
data = {
    "Personaje": ["Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki", "Satoru Gojo", "Kento Nanami"],
    "Misiones Completadas": [12, 28, 15, 150, 60],
    "Poder Estimado (Base 100)": [75, 82, 70, 999, 88]
}

# Crear un DataFrame de Pandas
df = pd.DataFrame(data)

# Mostrar la tabla en la web
st.subheader("Registro de Hechiceros")
st.dataframe(df)

# Mostrar un gráfico interactivo
st.subheader("Gráfica de Poder")
st.bar_chart(df.set_index("Personaje")["Poder Estimado (Base 100)"])