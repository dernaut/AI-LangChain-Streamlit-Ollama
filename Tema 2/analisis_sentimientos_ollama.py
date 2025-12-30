from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_ollama import OllamaLLM
import json

# Configuración del modelo
llm = OllamaLLM(model="deepseek-r1:latest", temperature=0.7)

# Preprocesador: limpia espacios y limita a 500 caracteres
def preprocesar_texto(texto: str) -> str:
    """Limpia el texto y limita su longitud a 500 caracteres."""
    return texto.strip()[:500]

preprocesador = RunnableLambda(preprocesar_texto)

# Generación de resumen
def generar_resumen(texto: str) -> str:
    """Genera un resumen del texto dado."""
    prompt = f"Resume en una sola oración sin opciones: {texto}"
    respuesta = llm.invoke(prompt)
    return respuesta

rama_resumen = RunnableLambda(generar_resumen)

def parsear_json(respuesta: str) -> str:
    """Extrae el contenido JSON de una respuesta de texto."""
    inicio = respuesta.find('{')
    fin = respuesta.rfind('}') + 1
    if inicio != -1 and fin != -1:
        return respuesta[inicio:fin]
    return '{}'

# Análisis de sentimientos con formato JSON
def analizar_sentimientos(texto: str) -> dict:
    """Analiza los sentimientos del texto y devuelve un diccionario con el resultado."""
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:

    {{"sentimiento": "positivo|negativo|neutral", "razon": "justificación breve"}}

    Texto: {texto}"""

    respuesta = llm.invoke(prompt)
    try:
        resultado = json.loads(parsear_json(respuesta))
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

resenas = [
    "Me encantó el producto, funcionó perfectamente y llegó a tiempo.",
    "El servicio fue terrible, no volveré a comprar aquí.",
    "El artículo está bien, pero podría ser mejor en algunos aspectos."
]


resultados_resenas = chain.batch(resenas)

resena_positiva = "Este producto es excelente y ha superado todas mis expectativas. Lo recomiendo a todos."
resena_negativa = "Estoy muy decepcionado con este servicio. No cumplió con lo que prometieron y fue una pérdida de dinero."

#resultado = chain.invoke(resena_negativa)

print (resultados_resenas)