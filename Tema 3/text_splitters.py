from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Cargar el documento PDF
loader = PyPDFLoader("C:\\Users\\jgiraldoc\\proyecto_langchain\\Tema 3\\QuijoteMancha.pdf")
pages = loader.load()

# Dividir el texto en fragmentos manejables
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(pages)


# Pasar el texto al LLM de Ollama
llm = OllamaLLM(model="deepseek-r1:latest", temperature=0.2)
summaries = []

i = 0
for chunk in chunks:
    if i > 10:
        break
    response = llm.invoke(f"has un resumen de los puntos mas importantes del siguiente texto:\n{chunk.page_content}")
    summaries.append(response)
    i += 1

final_summary = llm.invoke(f"Resume los siguientes puntos importantes en un solo resumen coherente:\n{''.join(summaries)}")

print("Resumen final del documento:")
print(final_summary)