# Librerías
import streamlit as st
import pandas as pd
import plotly_express as px


# Cargamos los datos
penguins_data = pd.read_csv('penguins.csv')

# Encabezado
st.title('Información sobre tres especies de pingüinos')
st.image('image.png', width=200)


# Mostrar tabla de datos
st.subheader(
    'Características físicas de 3 especies de pingüinos de la Antártida')

st.write('A continuación se muestran el conjunto de datos sobre tres especies. '
         'Contiene información sobre la isla, longitud y profundidad del pico, longitud de la aleta,'
         'masa corporal, sexo y año.'
         ' Con estos datos, crearemos algunos gráficos relevantes con el propósito de '
         'aprender las funciones de streamlit.')

# hide_index=True: para ocultar el índice
st.dataframe(penguins_data.head(15), hide_index=True)


# Línea horizontal
st.divider()


# ---------- Grafico 1: Recuento de especies por sexo ----------
st.subheader('Recuento de especies por sexo')

# Crear una casilla de verificación
casilla_barras = st.checkbox('¿Deseas mostrar el número de especies por sexo?')

# Agrupar datos para hacer el gráfico
filtro_especies_por_sexo = penguins_data.groupby(
    ['species', 'sex']).size().reset_index(name='recuento')

# Colores para cada sexo
colores_por_sexo = ['#FFE5B4', '#4169e1']

# Crear el gráfico si la casilla está activada
if casilla_barras:
    grafico1 = px.bar(filtro_especies_por_sexo,
                      x='species',
                      y='recuento',
                      color='sex',
                      color_discrete_sequence=colores_por_sexo,
                      text_auto=True  # Muestra los valores de cada barra
                      )

    # Mostrar el gráfico
    st.plotly_chart(grafico1, width='stretch')

    # Pie de gráfico
    st.caption('Gráfico 1: La cantidad pingüinos hembras y machos para cada especie es la misma, '
               'excepto para Gentoo, pero la diferencia es mínima.')


# ---------- Gráfico 2: Histograma de la masa corporal por especie ----------
st.subheader(
    'Frecuencia de la masa corporal de los pingüinos en gramos por especie')

# Seleccionar una especie
especie = st.selectbox("Selecciona una especie",
                       penguins_data['species'].unique())

# Filtrar los datos por especie
filtro_especie = penguins_data[penguins_data['species'] == especie]

# Crear el histograma
grafico2 = px.histogram(filtro_especie,
                        'body_mass_g',
                        title='Distribución de la masa corporal en gramos',
                        text_auto=True)

# Color de la barra del histograma
grafico2.update_traces(marker_color="#7CE7D9")

# Mostrar el histograma
st.plotly_chart(grafico2, width='stretch')

# Mostrar pie de gráfico para cada especie
if especie == 'Adelie':
    st.caption('Gráfico 2: La mayoría de los pinguinos Adelie pesan entre 3400 - 3990 gramos.'
               'El peso más bajo es 2800 gramos, pero se puede deber a diversos factores como la edad.')
elif especie == 'Gentoo':
    st.caption(
        'Gráfico 2: La mayoría de los pingüinos pesan entre 4600-5590 gramos')
else:
    st.caption(
        'Gráfico 2: La mayoría de los pingüinos pesan entre 3600-3790 gramos')


# ---------- Gráfico 3: Histograma del peso corporal por especie e isla ----------
st.subheader(
    'Frecuencia de la masa corporal de los pingüinos por especie e isla')

# Seleccionar la isla
isla = st.selectbox("Selecciona una isla",
                    penguins_data['island'].unique()
                    )

# Filtrar los datos por isla
filtro_isla = penguins_data[penguins_data['island'] == isla]

# Colores para cada especie
colores_por_especie = ["#6495ED", "#FF8C00", "#9CF37A"]

# Crear el gráfico
grafico3 = px.histogram(filtro_isla,
                        'body_mass_g',
                        color='species',
                        color_discrete_sequence=colores_por_especie,
                        title='Frecuencia del peso corporal en gramos para cada especie',
                        text_auto=True)

# Mostrar el historgrama
st.plotly_chart(grafico3, width='stretch')

# Mostrar pie de gráfico para cada especie
if isla == 'Torgersen':
    st.caption('Gráfico 3: En la isla Torgensen solo habitan pingüinos que pertenecen a la especie '
               'Adelie. Además, la mayoría de ellos pesan entre 3200-3790 gramos.')
elif isla == 'Biscoe':
    st.caption('Gráfico 3: En la isla Biscoe solo habitan pingüinos que pertenecen a la especie '
               'Adelie y Gentoo. Para la especie Adele, la mayoría pesa entre 3500-3990 gramos y '
               'para la especie Gentoo, pesan entre 4500-4990 gramos.')
else:
    st.caption('Gráfico 3: En la isla Dream solo habitan pingüinos que pertenecen a la especie '
               'Adelie y Chinstrap. Para ambas especies, la mayoría pesa entre 3400-3590 gramos.')


# --------- Gráfico 4: Relación entre longitud y profundidad del pico por especies ----------
st.subheader(
    'Relación entre la longitud y profundidad del pico en milímetros por especie')

# Crear una casilla de verificación
casilla_dispersion = st.checkbox(
    '¿Deseas mostrar la relación entre ambas variables?')

# Crear el gráfico si la casilla está activa
if casilla_dispersion:
    grafico4 = px.scatter(penguins_data,
                          x='bill_length_mm',
                          y='bill_depth_mm',
                          color='species',
                          title='Relación entre la longitud y profundidad del pico en milímetros')

    # Mostrar el gráfico
    st.plotly_chart(grafico4, width='stretch')

    # Mostrar pie de gráfico
    st.caption('Para las tres especies, notamos que hay relación positiva entre la '
               'longitud y profundidad del pico, es decir, a medida que aumenta la longitud, aumenta la profundidad.'
               ' Esto se puede deber a su alimentación, a su adaptación al hábitat, entre otros factores.')
