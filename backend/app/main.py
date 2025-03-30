from fastapi import FastAPI, Query
import pandas as pd
import re

app = FastAPI()

# Carregar os dados do CSV uma vez na memória
df = pd.read_csv("dados.csv")

@app.get('/search')
def search(q: str = Query(..., min_length=1)):
    # Filtrar produtos pelo nome
    q = re.sub(r"\s+", " ", q.strip())  # Limpa espaços extras
    palavras = q.split(" ")  # Divide a busca em palavras

    if len(palavras) > 1:
        # Adiciona um "s?" opcional apenas para a primeira palavra
        regex = rf"^{re.escape(palavras[0])}s?\b" + " " + " ".join(map(re.escape, palavras[1:]))
    else:
        # Se houver só uma palavra, usa apenas ela com "s?" opcional
        regex = rf"^{re.escape(q)}s?\b"

    # Aplica o filtro no DataFrame
    resultados = df[df["Produtos"].str.match(regex, case=False, na=False)]

    resultados = resultados.fillna("")  # Substitui NaN por strings vazias

    # Converter para dicionário
    return resultados.to_dict(orient="records")
