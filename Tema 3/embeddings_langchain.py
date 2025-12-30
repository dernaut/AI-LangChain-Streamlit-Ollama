from langchain_ollama import OllamaEmbeddings
import numpy as np

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

texto1 = "La capital de Francia es París."
texto2 = "París es un nombre común para mascotas."

vector1 = embeddings.embed_query(texto1)
vector2 = embeddings.embed_query(texto2)

print(vector1)
print(f"Dimensión de los vectores: {len(vector1)}")

cos_sim = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

print(f"Similitud coseno entre los textos vector1 y vector2: {cos_sim:.3f}")