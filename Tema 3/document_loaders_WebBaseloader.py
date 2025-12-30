from langchain_community.document_loaders import WebBaseLoader

cert_path = "C:\\Users\\jgiraldoc\\proyecto_langchain\\Tema 3\\indra_root_ca.pem"
loader = WebBaseLoader("https://en.wikipedia.org/wiki/Web_scraping", requests_kwargs={"verify": cert_path})

docs = loader.load()

print(docs)