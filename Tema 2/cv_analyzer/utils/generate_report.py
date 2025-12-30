from models.cv_model import AnalisisCV
import pandas as pd

def generar_csv(resultado: AnalisisCV):
    df = pd.DataFrame(resultado)
    csv_data = df.to_csv(index=False).encode('utf-8')
    return csv_data