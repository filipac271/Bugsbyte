from fastapi import FastAPI, Query
import pandas as pd
import re
import sys
import app.services.algorithm as algorithm

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


@app.get('/novopreco')
def novopreco(q: str = Query(..., min_length=1)):
    q = q.strip()  # Apenas remove espaços no início e no fim
    preconovo = algorithm.seasonal(q);
    return preconovo

@app.get('/unidades')
def unidades(q: str = Query(..., min_length=1)):
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

    # Acessa a coluna 'Preco' diretamente
    # Pega o valor da primeira linha e da coluna 'Preco' com iat
    preco_primeira_linha = resultados["Preco"].iat[0]

    print(preco_primeira_linha)
    precos_com_un =algorithm.extrair_preco_com_un(preco_primeira_linha)
    print(precos_com_un)

    return precos_com_un


