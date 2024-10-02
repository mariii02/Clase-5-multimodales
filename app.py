import streamlit as st
from PIL import Image

st.title("Mi primera chamba, me acuerdo del día en el que de la chamba yo me enamoré")

st.header ("Eladio carrion's story and why he is important to vallenato")

st.write ("""Su carrera musical profesional comenzó en 2015. Sin embargo, tiempo antes ya era conocido como influencer en Puerto Rico haciendo parodias imitando las voces de artistas de la escena urbana. Posterior a esto, incursionó como compositor.2​ En 2017 colaboró en el sencillo «Me enamoré de una yal», junto a Ñengo Flow y Ele A el Dominio, siendo este su primer éxito como artista.3​ Sin embargo, la canción que lo llevó al reconocimiento internacional fue «Mi cubana» con Cazzu, Khea y Ecko en 2018.4​ En 2019 recibió su primer nominación en los Premios Juventud como Nueva generación urbana. Participó en la Velada del año 3 creada por Ibai Llanos
En 2020 lanzó su álbum de estudio debut Sauce Boyz, el cual se posicionó en Top Latin Albums durante 10 semanas seguidas. Ese mismo año, recibió su primera nominación a los Premios Grammy Latinos por el sencillo «Kemba Walker» junto a Bad Bunny. En 2021, lanzó su segundo álbum Monarca, que estuvo nominado como mejor álbum de música urbana en los Grammy Latinos. Ese mismo año también colaboró en el sencillo «Eladio Carrión: BZRP Music Sessions, Vol. 40» junto a Bizarrap, que le valió una certificación de oro en España.""")

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
