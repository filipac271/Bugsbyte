import pandas as pd
from datetime import datetime

def isBestSoldMonth(productName):
    df = pd.read_csv('sample_sales_info_encripted.csv')
    filtered_df = df[df['product_dsc'].str.contains(productName, case=False, na=False)].copy()
    months[12]

    for index, row in filtered_df.iterrows():
        date = str(row['time_key'])
        month = int(date[4] + date[5])
        if months[month-1]==0:
            months[month-1]=1
        else:
            months[month-1]=months[month-1]+1

    maxMonth = max(months)
    today = datetime.now()
    if months[today.month-1] == maxMonth:
        return True
    else:
        return False

def increasesPrice(price):
    percentIncrease = 0.2
    newPrice = price + price*0.2
    return newPrice

def sazonalidade(productName, price):
    b = isBestSoldMonth(productName)
    if b:
        return increasesPrice(price)
    else:
        return price