import streamlit as st
from PIL import Image

st.title("Mejores libros que he leído en el año")

st.header ("Este año he leído 24 libros, 6 de esos han sido perfectos.")

st.write ("""Mi criterio para decidir qué libros han sido perfectos se basa meramente en mis gustos personales, como una lectora que disfruta de la temática fantástica y los ensayos de estudios feministas. Los libros que mencionaré no fueron necesariamente publicados este año, sino que corresponden a mi momento de lectura. Los recomiendo ampliamente.""")

image = Image.open("MejoresLibros.jpg")
st.image(image, caption = "1.Trenza del mar esmeralda/2.El último elfo/3.La era del mito/4.Las mujeres Weyward/5.Mujeres que corren con los lobos/6.Diosas, brujas y vampiresas")

texto = st.text_input("¿Cuál es tu libro favorito?", "Escribe tu libro favorito")
st.write("Tu libro favorito es:", texto)


col1, col2 = st.columns(2)

with col1:
  st.subheader("Leer es muy importante")
  st.write("¿Consideras que leer es muy importante?")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto!")

with col2:
  st.subheader("Interfaz multimodal")
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
