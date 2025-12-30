from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
import json

# Configuración del modelo
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)

# Preprocesador: limpia espacios y limita a 500 caracteres
def preprocesar_texto(texto: str) -> str:
    """Limpia el texto y limita su longitud a 500 caracteres."""
    return texto.strip()[:500]

preprocesador = RunnableLambda(preprocesar_texto)

# Generación de resumen
def generar_resumen(texto: str) -> str:
    """Genera un resumen del texto dado."""
    prompt = f"Resume en una sola oración: {texto}"
    respuesta = llm.invoke(prompt)
    return respuesta.content

rama_resumen = RunnableLambda(generar_resumen)

# Análisis de sentimientos con formato JSON
def analizar_sentimientos(texto: str) -> dict:
    """Analiza los sentimientos del texto y devuelve un diccionario con el resultado."""
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:

    {{"sentimiento": "positivo|negativo|neutral", "razon": "justificación breve"}}

    Texto: {texto}"""

    respuesta = llm.invoke(prompt)
    print(repr(respuesta.content))
    try:
        resultado = json.loads(respuesta.content)
    except json.JSONDecodeError:
        resultado = {"sentimiento": "neutro", "razon": "Error al analizar el sentimiento"}
    return resultado

rama_sentimiento = RunnableLambda(analizar_sentimientos)

# Combinación de resultados
def mezclar_resultados(data: dict) -> dict:
    """Combina el resumen y el análisis de sentimientos en una sola cadena."""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }

rama_mezcla = RunnableLambda(mezclar_resultados)

analisis_paralelo = RunnableParallel({
    "resumen": rama_resumen,
    "sentimiento_data": rama_sentimiento
})


# Cadena completa
chain = preprocesador | analisis_paralelo | rama_mezcla

resena = "Este producto es excelente y ha superado todas mis expectativas. Lo recomiendo a todos."

resultado = chain.invoke(resena)

print (resultado)