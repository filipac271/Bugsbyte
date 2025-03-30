import pandas as pd, numpy as np
import os
from datetime import timedelta, datetime
import re

filepathTransactions = os.path.join(os.path.dirname(__file__), '..', '..', 'sample_sales_info_encripted.csv')
filepathPrice        = os.path.join(os.path.dirname(__file__), '..', '..', 'sample_prod_info.csv')

# MEDIAN

def media(produto):
    table = pd.read_csv("dados.csv")
    table = table[table['Produtos'].apply(lambda x: str(x).lower().startswith(produto.lower()))].copy()
    
    table["preco_num"] = table['Preco'].apply(
        lambda x: str(x).split()[0].replace(",", ".") if pd.notna(x) else None
    )
    
    table = table.dropna(subset=["preco_num"])
    
    table['preco_num'] = table['preco_num'].astype(float)
    return table["preco_num"].mean()

# SEASONAL

def soldPerMonth(productName):
    df = pd.read_csv(filepathTransactions)
    
    filtered_df = df[df['product_dsc'].str.contains(productName, case=False, na=False)].copy()
    
    months = [0] * 12  
    for _, row in filtered_df.iterrows():
        date = str(row['time_key'])
        month = int(date[4:6]) 
        months[month - 1] += 1 

    totalBuys = sum(months)  
    
    if totalBuys == 0:
        return 0
    
    monthsPercentage = [month_count / totalBuys for month_count in months]
    
    today = datetime.now()
    return monthsPercentage[today.month - 1]  # Return the probability for the current month

def compute_c(max_value,curvature, mid_value):
    denominator = 1 + np.exp(-curvature * (50 - mid_value))
    c = 1 + (max_value/ denominator)
    return c

def f(familiarity,max_value, price, curvature, mid_value):
    c = compute_c(max_value,curvature,mid_value)
    value = - (max_value * price) / (1 + np.exp(-curvature * (familiarity - mid_value))) + c * price
    if (value < 0):
        return 0.02
    return value


def algorithm(familiarity,preco):
    max_value = 2
    curvature = 0.007
    mid_value = 50
    return f(familiarity,max_value,preco,-curvature,mid_value)


def extrair_preco_com_un(preco: str):
    # A expressão regular captura apenas a parte com o símbolo de euro e a unidade (exemplo: €/Kg)
    match = re.search(r"€/\w+", preco)
    if match:
        return match.group(0)  # Retorna apenas a parte "€/Kg", "€/un", etc.
    return None


def bundleDiscount (product):
    df = pd.read_csv(filepathTransactions)
    filtered_df = df[df['product_dsc'].apply(lambda x: str(x).lower().startswith(product.lower()))]
    if (filtered_df.empty == True):
        qtdAverage = 1
    else: 
        qtdAverage = round (filtered_df['qty'].mean())
    if qtdAverage == 1:
        message = "Este produto é geralmente vendido por si mesmo, logo não é recomendado nenhum desconto bundle."
    else:
        message = "É recomendado fazer descontos de \"Compre 1, leve " + str(qtdAverage) + "\"."
    return message

    
# main
def main (product):
    medium_price = media (product)
    print ("preço médio: "+ str(medium_price))
    fam = soldPerMonth (product)
    print (str(fam))
    ideal_price = algorithm (fam*600, medium_price)
    #print ("The ideal price is "+ str(round(ideal_price, 2)))
    return (round(ideal_price, 2))
