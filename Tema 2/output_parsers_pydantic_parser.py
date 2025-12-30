from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate


from pydantic import BaseModel, Field

class AnalisisTexto(BaseModel):
    resumen: str = Field(description="Resumen breve del texto.")
    sentimiento: str = Field(description="Sentimiento predominante del texto: positivo, negativo o neutral.")
    palabras_clave: list[str] = Field(description="Lista de palabras clave relevantes del texto.")

llm = OllamaLLM(model="deepseek-r1:latest", temperature=0.3)

parser = PydanticOutputParser(pydantic_object=AnalisisTexto)

prompt = PromptTemplate(
    template="""Eres un experto analista de texto. Analiza el siguiente texto con mucho cuidado y proporciona un análisis detallado.
    
    {format_instructions}
    
    Texto a analizar:
    {texto}
    
    Análisis:""",
    input_variables=["texto"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


chain = prompt | llm | parser


texto_prueba = """
La nueva película de ciencia ficción 'Stargate SG-1' es absolutamente 
espectacular. Los efectos visuales son impresionantes y la trama mantiene 
la tensión durante toda la película. Los actores principales entregan 
actuaciones convincentes que realmente te hacen creer en este mundo futurista.
Sin duda una de las mejores películas del año.
"""

try:
    # Invocar la cadena
    resultado = chain.invoke({"texto": texto_prueba})
    
    # Acceder a los datos
    print("=== RESULTADO DEL ANÁLISIS ===")
    print(f"Resumen: {resultado.resumen}")
    print(f"Sentimiento: {resultado.sentimiento}")
    print(f"Palabras clave: {', '.join(resultado.palabras_clave)}")
    
    # Exportar como JSON
    print("\n=== JSON RESULTANTE ===")
    print(resultado.model_dump_json(indent=2))
    
    # Exportar como diccionario
    dict_resultado = resultado.model_dump()
    print(f"\nTipo de objeto: {type(resultado)}")
    print(f"Tipo de diccionario: {type(dict_resultado)}")
    
except Exception as e:
    print(f"❌ Error durante el procesamiento: {e}")