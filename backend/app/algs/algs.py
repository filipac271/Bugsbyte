import pandas as pd



def media(produto):
    table = pd.read_csv("../../dados.csv")
    table = table[table["Produtos"].str.startswith(produto)]
    table["preco_num"] = table['Preco'].apply(lambda x: x.split()[0])
    table["preco_num"] = table["preco_num"].apply(lambda x: x.replace(",","."))
    table['preco_num'] = table['preco_num'].astype(float)
    print(table["preco_num"].mean())

media(input())
