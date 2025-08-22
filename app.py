import streamlit as st
from database import init_db, guardar_consulta
from utils import es_usuario_valido, buscar_imagenes_web, obtener_fecha_actual
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
init_db()

st.set_page_config(page_title="Chatbot Educativo", layout="centered")
st.title("🤖 Chatbot Educativo del Ecuador")
st.markdown("Consulta sobre temas educativos, técnicos y gubernamentales de Ecuador.")

usuario = st.text_input("🔐 Ingresa tu nombre completo o correo electrónico")

if usuario and not es_usuario_valido(usuario):
    st.error("Por favor ingresa un nombre completo (nombre y apellido) o un correo válido.")

consulta = st.text_area("✍️ Escribe tu consulta aquí:")
con_imagen = st.checkbox("¿Deseas obtener imágenes relacionadas (hasta 3)?")

if st.button("Enviar consulta"):
    if not usuario or not consulta:
        st.warning("Debes completar todos los campos.")
    elif not es_usuario_valido(usuario):
        st.error("Nombre o correo no válido.")
    else:
        st.markdown("⏳ Procesando tu consulta...")
        try:
            respuesta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Asistente experto en educación, tecnología y gobierno de Ecuador. Sé claro, amable y directo."},
                    {"role": "user", "content": consulta}
                ],
                temperature=0.5,
                max_tokens=350
            )
            texto_respuesta = respuesta.choices[0].message.content.strip()
            st.markdown("### 🤖 Respuesta:")
            st.success(texto_respuesta)

            if con_imagen:
                st.markdown("### 🖼️ Imágenes relacionadas:")
                urls = buscar_imagenes_web(consulta)
                for url in urls[:3]:
                    st.image(url, use_column_width=True)

            guardar_consulta(usuario, consulta, texto_respuesta, con_imagen, obtener_fecha_actual())
        except Exception as e:
            st.error("Hubo un error al procesar la consulta.")