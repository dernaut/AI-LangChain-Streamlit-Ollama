from langchain_ollama import OllamaLLM
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts
from models.cv_model import crear_cv_model_parser


def crear_evaluador_cv():
    modelo_base = OllamaLLM(
        model="deepseek-r1:latest",
        temperature=0.2
    )

    chat_prompt = crear_sistema_prompts()
    cadena_evulacion = chat_prompt | modelo_base | crear_cv_model_parser()

    return cadena_evulacion

def evaluar_candidato(texto_cv: str, descripcion_puesto: str) -> AnalisisCV:
    try:
        cadena_evaluacion = crear_evaluador_cv()
        resultado = cadena_evaluacion.invoke({
            "texto_cv": texto_cv,
            "descripcion_puesto": descripcion_puesto
        })
        return resultado
    except Exception as e:
        print(f"Error al evaluar el candidato: {e}")
        return AnalisisCV(
            nombre_candidato="",
            experiencia_años=0,
            habilidades_clave=[],
            nivel_educacion="",
            experiencia_relevante="",
            fortalezas=[],
            areas_mejora=[],
            porcentaje_ajuste=0,
            estado_procesamiento=False
        )