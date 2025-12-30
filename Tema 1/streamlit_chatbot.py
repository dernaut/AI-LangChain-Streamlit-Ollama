import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

# Configurar la página de la app
st.set_page_config(page_title="Chatbot con Google GenAI", page_icon="🤖")
st.title("Chatbot con Google GenAI Langchain 🤖")
st.markdown("Este es un chatbot simple utilizando Google GenAI a través de Langchain y Streamlit.")

with st.sidebar:
    st.header("Configuración del Chatbot")
    temperature = st.slider("Temperatura del modelo", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Selecciona el modelo", ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.5-flash-lite"])

    # Inicializar el modelo de chat con la configuración seleccionada
    chat_model = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)

# Inicializar el historial de chat en la sesión
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []


# Crear el template del prompt
prompt_template = PromptTemplate(
    input_variables=["mensaje", "historial"],
    template="""Eres un asistente útil y amigable llamado ChatBot ATM Pro. 
                
                Historial de conversación:
                {historial}

                Responde de manera clara y concisa a la siguiente pregunta: {mensaje}"""
)

# Crear cadena usando LCEL (Langchain Expression Language)
cadena = prompt_template | chat_model

# Mostrar mensajes previos en la interfaz streamlit
for mensaje in st.session_state.mensajes:
    if isinstance(mensaje, SystemMessage):
        # No mostrar el mensaje por pantalla
        continue

    role = "assistant" if isinstance(mensaje, AIMessage) else "user"

    with st.chat_message(role):
        st.markdown(mensaje.content)

# Eliminar conversación
if st.button("🗑️ Nueva conversación"):
    st.session_state.mensajes = []
    st.rerun()

# Entrada de usuario
pregunta = st.chat_input("Escribe tu mensaje aquí...")

if pregunta:
    # Mostrar el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Generar y mostrar respuesta del asistente
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            # Streaming de la respuesta
            for chunk in cadena.stream({"mensaje": pregunta, "historial": st.session_state.mensajes}):
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")  # Indicador de escritura

            response_placeholder.markdown(full_response)  # Respuesta completa sin indicador

        # Añadir el mensaje del usuario al historial
        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        # Añadir la respuesta del asistente al historial
        st.session_state.mensajes.append(AIMessage(content=full_response))

    except Exception as e:
        st.error(f"Se produjo un error al generar la respuesta: {str(e)}")
        st.info("Por favor, verifica tu configuración de Google GenAI y tu conexión a internet.")