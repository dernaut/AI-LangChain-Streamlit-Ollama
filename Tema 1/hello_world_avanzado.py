from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain

chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)


plantilla = PromptTemplate(
    input_variables=["nombre"],
    template="Saluda al usuario con su nombre y pregunta cómo está. \nNombre del usuario: {nombre}"
)

chain = plantilla | chat

resultado = chain.invoke({"nombre": "Carlos"})
print(resultado.content)