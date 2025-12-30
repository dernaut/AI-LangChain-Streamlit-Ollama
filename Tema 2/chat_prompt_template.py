from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


llm = OllamaLLM(model="deepseek-r1:latest", temperature=0.7)


chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un traductor del español al inglés muy preciso."),
    ("human", "{texto}")
])

mensaje = chat_prompt.invoke({"texto": "Hola, ¿cómo estás?"})

respuesta = llm.invoke(mensaje)

print(respuesta)