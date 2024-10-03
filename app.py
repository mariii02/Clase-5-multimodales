import streamlit as st
from PIL import Image

st.title("Mejores libros que he leído en el año")

st.header ("Este año he leído 24 libros, 6 de esos han sido perfectos.")

st.write ("""Mi criterio para decidir qué libros han sido perfectos se basa meramente en mis gustos personales, como una lectora que disfruta de la temática fantástica y los ensayos de estudios feministas. Los libros que mencionaré no fueron necesariamente publicados este año, sino que corresponden a mi momento de lectura. Los recomiendo ampliamente.""")

image = Image.open("EladioCarrion.jpg")
st.image(image, caption = "Eladio el bromas Carrion")

texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto!")

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz",("Visual","Auditiva", "Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Táctil":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de botones")
if st.button("Presiona el botón"):
  st.write("Gracias por presionar")
else:
  st.write("No has presionado aún")

with st.sidebar:
  st.subheader("Configura la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("Visual","Auditiva","Háptica")
  )
