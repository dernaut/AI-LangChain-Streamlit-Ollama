from pydantic import BaseModel, Field
from langchain_ollama import OllamaLLM

class AnalisisTexto(BaseModel):
    resumen: str = Field(description="Resumen breve del texto.")
    sentimiento: str = Field(description="Sentimiento predominante del texto: positivo, negativo o neutral.")

llm = OllamaLLM(model="deepseek-r1:latest", temperature=0.7)

structured_llm = llm.with_structured_output(AnalisisTexto)

texto_prueba = "Me encantó la película, fue una experiencia maravillosa y emocionante."

resultado = structured_llm.invoke(f"Analiza el siguiente texto: {texto_prueba}")

print(resultado)