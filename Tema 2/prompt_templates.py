from langchain_core.prompts import PromptTemplate

template = "Eres un experto en marketing. Sugiere un eslogan creativo para un producto llamado {producto}."

prompt = PromptTemplate(
    template = template,
    input_variables = ["producto"]
)

prompt_completo = prompt.format(producto="Arroz blanco")
print(prompt_completo)