import requests
from bs4 import BeautifulSoup
import pandas as pd, json, re

DADOS_PATH = "../../dados.csv"

DATAFRAME_COLUMNS = ["Produto", "Preco", "Loja", "Marca", "Categoria"]

CATEGORIES = ["Bebidas", "Charcutaria", "Congelados", "Cozinha", "Higiene e Beleza", "Bebé", "Lacticineos", "Mercearia", "Frutas e Legumes", "Gelados", "Peixe", "Carne", "Limpeza"]

CATEGORIES_FILTER_CONTINENTE = {
    "Bebidas":          ["bebidas"],          
    "Charcutaria":      ["charcutaria-queijo-charcutaria"],      
    "Congelados":       ["congelados"],
    "Cozinha":          ["casa-cozinha"],
    "Higiene e Beleza": ["higiene-beleza"],
    "Bebé":             ["bebe-ver-todos"],
    "Lacticineos":      ["laticinios"],
    "Mercearia":        ["mercearias"],
    "Frutas e Legumes": ["frutas-legumes-frutas","frutas-legumes-legumes"],
    "Gelados":          ["congelados-gelados"],
    "Peixe":            ["peixaria-e-talho-peixaria"],
    "Carne":            ["peixaria-e-talho-talho"],
    "Limpeza":          ["limpeza"]
}


CATEGORIES_FILTER_AUCHAN = {
    "Congelados" :      ["congelados"],
    "Cozinha" :         ["cozinha"],
    "Higiene e Beleza": ["higiene-corporal"],
    "Bebé" :            ["alimentacao-e-preparação","maternidade-amamentacao-1","fraldas-e-toalhitas","viagens-passeios","banho-higiene-1","biberoes-chupetas","quarto-do-bebe"],
    "Lacticineos":      ["produtos-lacteos"],
    "Mercearia":        ["mercearia"],
    "Frutas e Legumes": ["legumes-e-frutas"],
    "Gelados":          ["gelados-2"],
    "Peixe":            ["peixe"],
    "Carne":            ["carne"],
    "Limpeza":          ["limpeza-lavandaria"]
}

CATEGORIES_URL_PINGODOCE = {
    "Bebidas":          "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-bebidas&subcategorias&filtros&cp=",
    "Charcutaria":      "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-charcutaria&subcategorias&filtros&cp=",
    "Congelados":       "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-congelados&subcategorias&filtros&cp=" ,
    "Cozinha":          "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-cozinha-e-limpeza&subcategorias&filtros&cp=",
    "Higiene e Beleza": "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-higiene-e-beleza&subcategorias&filtros&cp=",
    "Bebé":             "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-infantil&subcategorias&filtros&cp=",
    "Lacticineos":      "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-lacticinios&subcategorias&filtros&cp=",
    "Mercearia":        "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-mercearia&subcategorias&filtros&cp=",
    "Frutas e Legumes": "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-frescos-embalados&subcategorias&filtros&cp=",
    "Gelados":          "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-congelados&subcategorias=pingo-doce-congelados-gelados&filtros&cp=",
    "Peixe":            "https://www.pingodoce.pt/produtos/marca-propria-pingo-doce/pingo-doce/?q&o=maisbaixo&categoria=pingo-doce-congelados&subcategorias=pingo-doce-congelados-peixe-e-marisco&filtros&cp="
}

# utils

def capitalizeExcept(text, exceptions_down=None):
    if exceptions_down is None:
        exceptions_down = set()  # words to force lowercase
    
    words = text.split()
    processed_words = []
    
    for word in words:
        lower_word = word.lower()
        if lower_word in (ex.lower() for ex in exceptions_down):
            processed_words.append(word.lower())
        else:
            processed_words.append(word.capitalize())
    
    return " ".join(processed_words)

# continente

def getContinenteProduct(soup, category):
    productsData = []
    products = soup.find_all("div", class_="product-tile")
    for product in products:
        product_description = product.find("h2", class_="pwc-tile--description")
        if product_description:
            nome = product_description.text.strip()
        else:
            data_brandid = product.get("data-brandid", "")
            data_id = product.get("id", "")
            if data_brandid and data_id:
                nome = data_brandid
            else:
                nome = ""
        preco_tag_secundary = product.find ("div", class_ = "pwc-tile--price-secondary col-tile--price-secondary")
        if preco_tag_secundary:
            preco = preco_tag_secundary.find("span", class_="ct-price-value").text.strip()
            preco = preco[1:] + " " + preco[0] # swap € symbol from beginning to end
            preco = preco + preco_tag_secundary.find ("span", class_ = "pwc-m-unit").text.strip()
        else:
            preco = product.get("data-price", "")
            
        loja = "Continente"
        
        marca_tag = product.find("p", class_="pwc-tile--brand")
        if marca_tag:
            marca = marca_tag.text.strip()
        else:
            marca = "Unknown"
            
        categoria = category
        productsData.append([nome, preco, loja, marca, categoria])
    
    return productsData
    

def scrapeContinente():
    print("Starting to scrape Continente")
    baseURL = "https://www.continente.pt/on/demandware.store/Sites-continente-Site/default/Search-UpdateGrid"
    PAGE_SIZE = 36  
    df = pd.DataFrame(columns=DATAFRAME_COLUMNS)

    for cat in CATEGORIES:
        print(f"Starting the {cat} category")
        categoryFilters = CATEGORIES_FILTER_CONTINENTE.get(cat, [])

        for categoryFilter in categoryFilters:
            start = 0

            while True:  
                params = {
                    "cgid": categoryFilter, 
                    "pmin": "0.01", 
                    "start": start,  
                    "sz": PAGE_SIZE
                }
                response = requests.get(baseURL, params=params)
                print(response.url)

                if response.status_code != 200:
                    print(f"Error accessing {cat}: {response.status_code}")
                    break

                soup = BeautifulSoup(response.text, "html.parser")
                prodData = getContinenteProduct(soup, cat)

                if not prodData: 
                    print(f"No more products in {cat}, moving to next")
                    break

                new_rows = pd.DataFrame(prodData, columns=DATAFRAME_COLUMNS)
                df = pd.concat([df, new_rows], ignore_index=True)

                start += PAGE_SIZE  

    df.to_csv(DADOS_PATH, mode='a', index=False, encoding="utf-8", header=False)
    return df
  

# auchan

def getAuchanProduct(soup, category):
    productsData = []
    products = soup.find_all("div", class_="auc-product")
    count = 1
    
    for product in products:
        if count % 100 == 0:
            print("read " + str(count) + " products of the " + category + " category")
        count += 1
        
        nome = ""
        marca = "Unknown"
        preco = ""
        
        product_title = product.find("div", class_="product-tile")
        if product_title and product_title.get("data-gtm"):
            try:
                gtm_data = json.loads(product_title.get("data-gtm"))
                nome = gtm_data.get("name", "")
                marca = gtm_data.get("brand", "")
            except (json.JSONDecodeError, TypeError):
                pass
        
        if not nome:
            product_name_div = product.find("div", class_="auc-product-tile__name")
            if product_name_div:
                nome = product_name_div.text.strip()
        
        price_span = product.find("span", class_="auc-measures--price-per-unit")
        if price_span:
            preco = price_span.text.strip()
        nome = nome.replace (marca, "").strip()
        nome = capitalizeExcept(nome, exceptions_down={"de", "a", "e"})
        nome = " ".join (nome.split()) # remove double whitespaces
        marca = marca.capitalize()

        loja = "Auchan"
        categoria = category
        productsData.append([nome, preco, loja, marca, categoria])
    
    return productsData



def scrapeAuchan():
    print("Starting to scrape Auchan")
    baseURL = "https://www.auchan.pt/on/demandware.store/Sites-AuchanPT-Site/pt_PT/Search-UpdateGrid"
    PAGE_SIZE = 1000  
    df = pd.DataFrame(columns=DATAFRAME_COLUMNS)

    for cat in CATEGORIES:
        print(f"Starting the {cat} category")
        categoryFilters = CATEGORIES_FILTER_AUCHAN.get(cat, [])

        for categoryFilter in categoryFilters:
            start = 0

            while True: 
                params = {
                    "cgid": categoryFilter,
                    "prefn1": "soldInStores",
                    "prefv1": "000",
                    "srule": "Best seller",
                    "start": start,
                    "sz": PAGE_SIZE,
                    "next": "true"
                }
                response = requests.get(baseURL, params=params)
                print(response.url)

                if response.status_code != 200:
                    print(f"Error accessing {cat}: {response.status_code}")
                    break

                soup = BeautifulSoup(response.text, "html.parser")
                prodData = getAuchanProduct(soup, cat)

                if not prodData: 
                    print(f"No more products in {cat}, moving to next")
                    break

                new_rows = pd.DataFrame(prodData, columns=DATAFRAME_COLUMNS)
                df = pd.concat([df, new_rows], ignore_index=True)

                start += PAGE_SIZE  

    df.to_csv(DADOS_PATH, mode='a', index=False, encoding="utf-8", header=False)
    return df

#pingo doce

def getPingoDoceProduct(soup, category):
    productsData = []
    cards_wrapper = soup.find("div", class_="cards-wrapper js-card-list-wrapper")
    products = cards_wrapper.find_all("div", class_="product-cards")
    
    for product in products:
        nome = product.find("h3", class_ = "product-cards__title").text.strip()
        preco = product.find("span", class_ = "product-cards_price").text.strip()

        marca = "Pingo Doce"
        loja = "Pingo Doce"

        if marca in nome:
            nome = nome.replace(marca, "").strip()
            nome = " ".join (nome.split())
        
        preco = re.sub(r"(\d+\.?\d*)€\s*/\s*([A-Za-z]+)", r"\1 €/\2", preco) # correct formatting (moving the €)
        categoria = category
        productsData.append([nome, preco, loja, marca, categoria])
        
    return productsData
    

def scrapePingoDoce ():
    print ("Starting to scrape Pingo Doce")
    df = pd.DataFrame (columns=DATAFRAME_COLUMNS)

    for cat in CATEGORIES:
        print ("starting the "+ cat + " category")
    
        start = 1
        base_url = CATEGORIES_URL_PINGODOCE.get(cat)
        if base_url == None:
            continue
        while True: 
            url = base_url + str (start)
            
            response = requests.get(url)
            print (response.url)
            if response.status_code != 200:
                print(f"Erro ao acessar à página {cat}: {response.status_code}")
                break
    
            soup = BeautifulSoup (response.text, "html.parser")
            prodData = getPingoDoceProduct (soup, cat)
            
            if len(prodData) == 0:
                print (f"No more products in {cat}, moving to next")
                break

            new_rows = pd.DataFrame(prodData, columns=DATAFRAME_COLUMNS)
            df = pd.concat([df, new_rows], ignore_index=True)
            start += 1 
    df.to_csv(DADOS_PATH, mode='a', index=False, encoding="utf-8", header=False)                                            
    return df
  



# main
mainDf = pd.DataFrame(columns= DATAFRAME_COLUMNS)

auchanDf = scrapeAuchan ()

pingodoceDf = scrapePingoDoce()

continenteDf = scrapeContinente ()

