from langchain_google_community import GoogleDriveLoader

credentials_path = "C:\\Users\\jgiraldoc\\proyecto_langchain\\Tema 3\\client_credential.json"
token_path = "C:\\Users\\jgiraldoc\\proyecto_langchain\\Tema 3\\token.json"


loader = GoogleDriveLoader(
    folder_id="root",
    credentials_path=credentials_path,
    token_path=token_path,
    recursive=True,
)

documents = loader.load()
print(documents)