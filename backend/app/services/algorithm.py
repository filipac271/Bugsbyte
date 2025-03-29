import pandas as pd, numpy as np
import os
from datetime import timedelta, datetime


filepathTransactions = os.path.join(os.path.dirname(__file__), '..', '..', 'sample_sales_info_encripted.csv')
filepathPrice        = os.path.join(os.path.dirname(__file__), '..', '..', 'sample_prod_info.csv')


# ELASTIC PRICE - how sensitive the loss in sells is to the rise of price

def getQtdPerWeek (product):
    df = pd.read_csv(filepathTransactions)
    product.upper()

    filtered_df = df[df['product_dsc'].str.startswith(product.lower())].copy()
    
    if filtered_df.empty:
        print ("No data, product not found")
        return None
    
    if not pd.api.types.is_datetime64_any_dtype(filtered_df['time_key']):
            filtered_df['time_key'] = pd.to_datetime(filtered_df['time_key'], format='%Y%m%d')
    
    filtered_df['tuesday'] = filtered_df['time_key'].apply(
        lambda x: x - timedelta(days=x.weekday()) + timedelta(days=1) 
    )
    
    weekly_totals = filtered_df.groupby('tuesday')['qty'].sum()
    
    result_dict = {date.strftime('%Y%m%d'): qty for date, qty in weekly_totals.items()}
    print (result_dict)
    return result_dict

def getPricePerWeek (product):
    df = pd.read_csv (filepathPrice, delimiter=";")
    filtered_df = df[df['product_dsc'].str.contains(product, case=False, na = False)].copy()
    if filtered_df.empty:
        print ("No data, product not found")
        return None
    non_date_columns = ["sku", "product_dsc", "cat_cd", "cat_dsc_ext", "product_short_dsc"]
    date_columns = [col for col in filtered_df.columns if col not in non_date_columns]

    return filtered_df[date_columns].iloc[0].to_dict()
    



def calculatePriceElasticity(quantity_dict, price_dict):
    common_dates = sorted(set(quantity_dict.keys()) & set(price_dict.keys()))
    
    if len(common_dates) < 2:
        return {"error": "Need at least two weeks of data"}
    
    results = {}
    
    for i in range(1, len(common_dates)):
        current_date = common_dates[i]
        previous_date = common_dates[i-1]
        
        q1 = quantity_dict[previous_date]
        q2 = quantity_dict[current_date]
        p1 = price_dict[previous_date]
        p2 = price_dict[current_date]
        
        if p1 == p2 or q1 == 0 or p1 == 0:
            elasticity = None  
        else:
            percent_change_quantity = (q2 - q1) / q1
            percent_change_price = (p2 - p1) / p1
            
            if abs(percent_change_price) > 0.1:  # if price change is large
                avg_q = (q1 + q2) / 2
                avg_p = (p1 + p2) / 2
                elasticity = ((q2 - q1) / avg_q) / ((p2 - p1) / avg_p)
            else:
                # standard elasticity formula
                elasticity = percent_change_quantity / percent_change_price
            
            elasticity = abs(elasticity)
        
        if elasticity is not None and np.isfinite(elasticity):
            results[current_date] = elasticity
    
    # average elasticity
    valid_elasticities = [e for e in results.values() if not np.isnan(e) and np.isfinite(e)]
    if valid_elasticities:
        results["average_elasticity"] = sum(valid_elasticities) / len(valid_elasticities)
    
    return results


def get_last_tuesday(reference_date=None):
    if reference_date is None:
        reference_date = datetime.now()
    else:
        reference_date = datetime.strptime(reference_date, '%Y-%m-%d')
    days_since_tuesday = (reference_date.weekday() - 1) % 7
    last_tuesday = reference_date - timedelta(days=days_since_tuesday)
    return last_tuesday.strftime('%Y-%m-%d')


def predict_elasticity(elasticity_data, current_date_str, weights=[0.6, 0.4]):
    current_date = datetime.strptime(current_date_str, '%Y-%m-%d')
    tuesday_date = get_last_tuesday(current_date)
    
    year_2023_date = datetime(
        year=2023, 
        month=tuesday_date.month, 
        day=tuesday_date.day
    ).strftime('%Y-%m-%d')
    
    year_2022_date = datetime(
        year=2022,
        month=tuesday_date.month,
        day=tuesday_date.day
    ).strftime('%Y-%m-%d')

    e_2023 = elasticity_data.get(year_2023_date)
    e_2022 = elasticity_data.get(year_2022_date)
    
    available_data = []
    if e_2023 is not None:
        available_data.append((e_2023, weights[0]))
    if e_2022 is not None:
        available_data.append((e_2022, weights[1]))
    
    if not available_data: 
        return None
    
    predicted_elasticity = sum(e * w for e, w in available_data) / sum(w for _, w in available_data)
    return predicted_elasticity


def calculate_ideal_price(base_price, elasticity):
    if elasticity is None:
        return base_price
    if abs(elasticity) < 1: 
        return base_price * (2 - abs(elasticity))
    return base_price * (1 + 1 / elasticity)


def calculate_ideal_price_based_on_price_elasticity(product, precoBase):
    qtd = getQtdPerWeek(product)
    price = getPricePerWeek(product)
    dictElasticity = calculatePriceElasticity(qtd, price)
    elasticity_now = predict_elasticity (dictElasticity, datetime.now)
    return calculate_ideal_price (precoBase, elasticity_now)
