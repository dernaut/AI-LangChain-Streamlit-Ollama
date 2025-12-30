from langchain_core.messages import HumanMessage,  AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente útil que mantiene el contexto de la conversación."),
    MessagesPlaceholder(variable_name="historial"),
    ("human", "{pregunta_actual}")
])

#Simulamos un historial de conversación
historial_conversacion = [
    HumanMessage(content="Hola, ¿cómo estás?"),
    AIMessage(content="¡Hola! Estoy bien, gracias. ¿En qué puedo ayudarte hoy?"),
    HumanMessage(content="¿Puedes contarme un chiste?"),
    AIMessage(content="Claro, aquí tienes uno: ¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 es igual a DEC 25."),
    HumanMessage(content="¡Jajaja! Muy bueno. ¿Cuál es la capital de Francia?"),
    AIMessage(content="La capital de Francia es París.")
]


mensajes = chat_prompt.format_messages(
    historial = historial_conversacion,
    pregunta_actual = "¿Cuál es la capital de España?"
)

for mensaje in mensajes:
    print(mensaje.content)

