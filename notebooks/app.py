import streamlit as st
import pandas as pd
import plotly_express as px

penguins_data = pd.read_csv('../penguins.csv')

# ----- Encabezado ----
st.header('Información sobre especies de pingüinos')

# ----- Mostrar tabla de datos -----
st.subheader('Dataset')

st.dataframe(penguins_data)

# ----- Botón para mostrar un histograma-----
boton_hist = st.button('Construir un histograma')

# Lógica para actiar el botón
if boton_hist:
    st.write(
        'Histograma que muestra la frecuencia de la longitud de la aleta del pinguino en mm')

    # Creación del histograma
    fig = px.histogram(penguins_data, 'flipper_length_mm')

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# ----- Botón para mostrar un gráfico de dispersión ----
boton_disp = st.button('Construir un diagrama de dispersión')

if boton_disp:

    # Creación del diagrama
    diagrama = px.scatter(penguins_data, 'bill_length_mm', 'body_mass_g')

    # Mostrar el diagrama
    st.plotly_chart(diagrama, use_container_width=True)
