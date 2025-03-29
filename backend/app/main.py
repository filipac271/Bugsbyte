from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

# Carregar os dados do CSV uma vez na memória
df = pd.read_csv("dados.csv")

@app.get('/search')
def search(q: str = Query(..., min_length=1)):
    # Filtrar produtos pelo nome
    resultados = df[df["Produtos"].str.contains(q, case=False, na=False)]

    resultados = resultados.fillna("")  # Substitui NaN por strings vazias

    # Converter para dicionário
    return resultados.to_dict(orient="records")
