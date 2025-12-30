import PyPDF2
from io import BytesIO

def extraer_texto_pdf(archivo_pdf):
    """
    Extrae el texto de un archivo PDF.
    """
    try:
        lector_pdf = PyPDF2.PdfReader(BytesIO(archivo_pdf.read()))
        texto_completo = ""

        for numero_pagina, pagina in enumerate(lector_pdf.pages, start=1):
            texto_pagina = pagina.extract_text()
            if texto_pagina.strip():
                texto_completo += f"\n-- Página {numero_pagina} --\n"
                texto_completo += texto_pagina + "\n"
        
        texto_completo = texto_completo.strip()

        if not texto_completo:
            raise ValueError("El PDF no contiene texto extraíble.")

        return texto_completo
    
    except Exception as e:
        raise ValueError(f"Error al procesar el archivo PDF: {e}")