from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class AnalisisCV(BaseModel):
    """Modelo de datos para representar el análisis de un CV de candidato."""

    nombre_candidato: str = Field(description="Nombre completo del candidato extraído del CV")
    experiencia_años: int = Field(description="Número total de años de experiencia laboral relevante del candidato")
    habilidades_clave: list[str] = Field(description="Lista de las 5-7 habilidades clave extraídas del CV")
    nivel_educacion: str = Field(description="Nivel educativo más alto alcanzado por el candidato")
    experiencia_relevante: str = Field(description="Resumen breve de la experiencia laboral más relevante del candidato para el puesto")
    fortalezas: list[str] = Field(description="Lista de las 3-5 principales fortalezas del candidato basadas en el análisis del CV")
    areas_mejora: list[str] = Field(description="Lista de las 3-5 principales áreas de mejora del candidato basadas en el análisis del CV")
    porcentaje_ajuste: int = Field(description="Porcentaje de ajuste del candidato para el puesto (0-100) basado en el análisis del CV", ge=0, le=100)
    estado_procesamiento: bool = Field(default=True, description="Indica si el procesamiento del CV fue exitoso o si hubo un error")


def crear_cv_model_parser() -> PydanticOutputParser:
    """Crea y devuelve un parser de salida Pydantic para el modelo AnalisisCV."""
    return PydanticOutputParser(pydantic_object=AnalisisCV)