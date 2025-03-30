import pandas as pd, numpy as np
import os
from datetime import timedelta, datetime


filepathTransactions = os.path.join(os.path.dirname(__file__), '..', '..', 'sample_sales_info_encripted.csv')
filepathPrice        = os.path.join(os.path.dirname(__file__), '..', '..', 'sample_prod_info.csv')

# MEDIUM

def media(produto):
    table = pd.read_csv("../../dados.csv")
    table = table[table['Produtos'].apply(lambda x: x.lower().startswith(produto.lower()))].copy()

    #table = table[table["Produtos"].str.startswith(produto)]
    table["preco_num"] = table['Preco'].apply(lambda x: x.split()[0])
    table["preco_num"] = table["preco_num"].apply(lambda x: x.replace(",","."))
    table['preco_num'] = table['preco_num'].astype(float)
    return table["preco_num"].mean()
    

# main
def main ():
    product = input("Produto: ")
    medium_price = media (product)
    print ("preço médio: "+ str(medium_price))
    
    #print ("The ideal price is "+ str(round(ideal_price, 2)))


if __name__ == "__main__":
    main()
