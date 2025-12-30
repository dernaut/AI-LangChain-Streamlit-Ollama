from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:/Users/jgiraldoc/Desktop/cv_jgiraldoc.pdf")

pages = loader.load()

for i, page in enumerate(pages):
    print(f"=== Pagina {i + 1} ===")
    print(f"Contenido: {page.page_content}")
    print(f"Metadatos: {page.metadata}")